# This script is created so that the repetitive tasks can scheduled for data analysis 

# %pip install pandas
# %pip install sqlalchemy

import pandas as pd 
import sqlite3
import os
import logging
import time
from ingestion_db import ingest_db


logging.basicConfig(
    filename = "D:/kaif2/04_Projects/Data_Analyst/Python/Vendor_Performance/Logs/Get_Vendor_Summary.log",
    level= logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode= "a"
)
 
def create_vendor_summary(conn):
    ''' This func will merge the different tables to get the overall vendor summary and adding new columns in the resultant data '''    
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS(
                                         SELECT
                                            VendorNumber,
                                            SUM(freight) AS FreightCost
                                         FROM vendor_invoice
                                         GROUP BY VendorNumber
                                         ),
                                         
                                         PurchaseSummary AS (
                                         SELECT 
                                            p.VendorNumber,
                                            p.VendorName,
                                            p.Brand,
                                            p.Description,
                                            p.PurchasePrice,
                                            pp.Price AS ActualPrice,
                                            pp.Volume,
                                            SUM(p.Quantity) AS TotalPurchaseQuantity,
                                            SUM(p.Dollars) AS TotalPurchaseDollars
                                         FROM Purchases p 
                                         JOIN Purchase_Prices pp
                                            ON p.Brand = pp.Brand
                                         WHERE p.PurchasePrice > 0
                                         GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
                                         ),

                                         SalesSummary AS (
                                         SELECT
                                            VendorNo,
                                            Brand,
                                            SUM(SalesQuantity) AS TotalSalesQuantity,
                                            SUM(SalesDollars) AS TotalSalesDollars,
                                            SUM(SalesPrice) AS TotalSalesPrice,
                                            SUM(ExciseTax) AS TotalExciseTax
                                          FROM Sales
                                         GROUP BY VendorNo, Brand
                                         )

                                         SELECT
                                            ps.VendorNumber,
                                            ps.VendorName,
                                            ps.Brand,
                                            ps.Description,
                                            ps.PurchasePrice,
                                            ps.ActualPrice,
                                            ps.Volume,
                                            ps.TotalPurchaseQuantity,
                                            ps.TotalPurchaseDollars,
                                            ss.TotalSalesQuantity,
                                            ss.TotalSalesDollars,
                                            ss.TotalSalesPrice,
                                            ss.TotalExciseTax,
                                            fs.FreightCost
                                         FROM PurchaseSummary ps
        
                                         LEFT JOIN SalesSummary ss
                                            ON ps.VendorNumber = ss.VendorNo
                                            AND ps.Brand == ss.Brand
                                         LEFT JOIN FreightSummary fs
                                            ON ps.VendorNumber = fs.VendorNumber
                                         ORDER BY ps.TotalPurchaseDollars DESC
                                         """, conn)
    return vendor_sales_summary



def clean_data(df):
   ''' This func will clean data '''

   # changing datatype to float:
   df['Volume'] = df['Volume'].astype('float64')

   # filling missing values with 0:
   df.fillna(0, inplace=True)

   # removing spaces from categorical columns (handle possible column-name casing):
   if 'VendorName' in df.columns:
      df['VendorName'] = df['VendorName'].astype(str).str.strip()

   # SQL/DB columns are usually lowercase; be defensive and accept either
   if 'Description' in df.columns:
      df['Description'] = df['Description'].astype(str).str.strip()

   # creating new columns for better analysis:
   df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
   df['ProfitMargin'] = (df['GrossProfit']/df['TotalSalesDollars'])*100
   df['StockTurnover'] = df['TotalSalesQuantity']/ df['TotalPurchaseQuantity']
   df['SalestoPurchaseRatio'] = df['TotalSalesDollars']/ df['TotalPurchaseDollars']

   return df


if __name__ == "__main__":
   # creating database connection
   start = time.time()

   
   conn = sqlite3.connect('D:/kaif2/04_Projects/Data_Analyst/Python/Vendor_Performance/Data/Inventory.db')

   logging.info('Creating Vendor Summary Table.....')
   summary_df = create_vendor_summary(conn)
   logging.info(summary_df.head())

   logging.info('Cleaning Data.....')
   clean_df = clean_data(summary_df)
   logging.info(clean_df.head())

   # save cleaned vendor summary as CSV
   csv_path = r"D:/kaif2/04_Projects/Data_Analyst/Python/Vendor_Performance/Data/vendor_sales_summary.csv"
   os.makedirs(os.path.dirname(csv_path), exist_ok=True)
   try:
      clean_df.to_csv(csv_path, index=False, encoding='utf-8')
      logging.info(f"Saved vendor summary CSV to {csv_path}")
   except Exception as e:
      logging.error(f"Failed to save vendor summary CSV: {e}")

   logging.info('Ingesting data.....')
   # write cleaned dataframe to sqlite database (replace existing summary table)
   # clean_df.to_sql('vendor_sales_summary', conn, if_exists='replace', index=False)
   ingest_db(clean_df, 'vendor_sales_summary', conn, if_exists='replace')

   end = time.time()
   total_time = (end-start)/60
   logging.info("--------------Ingestion Completed--------------")
   logging.info(f"Total Time Taken: {total_time} minutes")