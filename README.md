<div align="center">
  <img width="320px" src="Images/logo.png" />
</div>

<h1 align="center">MerchX Supplier Profitability & Dependency Risk Analysis</h1>

<h3 align="center">Industry: Retail / Wholesale | Supply Chain & Procurement Analytics</h3>

---

<table align="center">
  <tr>
    <td width="1440">
<h2 align="center">Client Background</h2>

<p>
MercX is a mid-to-large retail and wholesale enterprise managing a diverse supplier base across multiple product categories faced growing challenges in balancing profitability, inventory efficiency, and supplier dependency. Despite strong sales performance, leadership lacked visibility into which vendors were driving sustainable profit versus locking capital in slow-moving inventory.
</p>

<p>
At the time of analysis, the client was facing rising inventory holding costs and increased dependency on a small set of vendors due to limited vendor-level performance transparency and reactive procurement decisions.
</p>

<p>
Reporting to the <strong>Procurement, Finance, and Operations Teams</strong>, an end-to-end analysis was conducted using <strong>SQL, Python, and Power BI</strong>. The engagement aimed to shift the organization from reactive purchasing to a <strong>proactive, data-driven sourcing and inventory strategy</strong>.
</p>

<strong>Key Focus Areas of the Analysis:</strong>
<ul>
  <li>Quantifying supplier contribution, profitability, and dependency risk.</li>
  <li>Identifying slow-moving inventory and capital lock-in drivers.</li>
  <li>Building an interactive <strong>Power BI Vendor Performance Dashboard</strong> for decision-makers.</li>
</ul>

<p>
The insights and recommendations support <strong>executive decision-making and procurement strategy</strong>, with the objective of improving profitability, reducing operational risk, and optimizing working capital.
</p>

  </td>
  </tr>
</table>

---

<h2 align="center">Executive Summary</h2>
<table align="center">
  <tr>
    <td width="1440">
      <body>
        The organization lacked a unified view of supplier profitability, inventory efficiency, and procurement risk. This project delivers a <strong>Vendor Performance & Risk Analytics Dashboard</strong> combining descriptive, diagnostic, and statistical analysis to help the business move from <em>reactive purchasing</em> to <em>proactive, insight-driven decision-making</em>.
        <br><br>

<strong>High-Level Business Impact:</strong>
        <ul>
          <li>Identified <strong>72% reduction in unit cost</strong> for large-volume purchases compared to small orders.</li>
          <li>Revealed <strong>80%+ procurement dependency</strong> on a limited set of top vendors.</li>
          <li>Quantified <strong>millions in capital locked</strong> in unsold inventory driven by low stock-turnover vendors.</li>
          <li>Validated statistically significant profit margin differences between top- and low-performing vendors (p &lt; 0.05).</li>
        </ul>

<strong>Outcome: Power BI Vendor Performance Dashboard</strong>
        <ul>
          <li>Provides real-time visibility into vendor profitability and inventory risk.</li>
          <li>Flags supplier dependency and slow-moving inventory before impacting cash flow.</li>
          <li>Enables targeted pricing, sourcing, and inventory optimization strategies.</li>
        </ul>
      </body>
    </td>
  </tr>
</table>

---

<h2 align="center">Dashboard Walkthrough</h2>

<table align="center">


 <tr>
    <td align="center">
      <a href="/Images/Dashboard.png" target="_blank">
        <img src="/Images/Dashboard.png" 
              alt="Vendor Performance Visuals"
              style="max-width:100%; height:auto; border-radius:10px;" />
      </a>
      <p><strong>Vendor Pareto, Inventory Risk & Profitability Analysis</strong></p>
    </td>
  </tr> 
</table>

---

<h2 align="center">Business Problem</h2>
<table align="center">
  <tr>
    <td width="1440">
<body>
The organization was experiencing <strong>inefficient capital utilization and supplier concentration risk</strong> but lacked clarity on:
<ul>
  <li>Which vendors contributed most to procurement spend and dependency.</li>
  <li>Which suppliers and brands underperformed despite healthy margins.</li>
  <li>Where inventory turnover was insufficient, leading to excess stock.</li>
</ul>

Without analytical visibility, procurement strategies remained reactive—resulting in margin erosion, excess inventory, and elevated operational risk.
<br><br>
<strong>Objective:</strong>
Build a vendor analytics framework that answers:
<ul>
  <li><em>Who drives profitability and risk?</em></li>
  <li><em>Why do margin and volume patterns differ across vendors?</em></li>
  <li><em>Where should procurement and inventory strategies be optimized?</em></li>
</ul>
</body>
</td>
  </tr>
</table>

---

<h2 align="center">Methodology & Analytical Approach</h2>
<table align="center">
  <tr>
    <td width="1440">
<ul>
  <li><strong>Exploratory Data Analysis (EDA):</strong> Assessed distributions, outliers, and correlations across purchase, sales, margin, and inventory metrics.</li>
  <li><strong>Diagnostic Analysis:</strong> Vendor and brand-level segmentation to isolate profitability and dependency drivers.</li>
  <li><strong>Statistical Analysis:</strong> Confidence intervals and two-sample t-tests to validate profit margin differences.</li>
  <li><strong>BI Modeling:</strong> DAX-based ranking, Pareto logic, and KPI modeling for interactive analysis.</li>
</ul>

<strong>Why this approach?</strong><br>
Combining descriptive BI with statistical validation ensured insights were not only visible but defensible for executive decision-making.
    </td>
  </tr>
</table>

---

<h2 align="center">Skills & Tools Used</h2>
<table align="center">
  <tr>
    <td width="1440">
<ul>
  <li><strong>Data Analysis:</strong> Python (Pandas, NumPy, SciPy)</li>
  <li><strong>Statistics:</strong> Hypothesis Testing, Confidence Intervals, Correlation Analysis</li>
  <li><strong>Data Visualization:</strong> Power BI, DAX, Interactive Dashboards</li>
  <li><strong>Business Analytics:</strong> Profitability Analysis, Pareto Analysis, Inventory Turnover</li>
  <li><strong>SQL & Data Modeling:</strong> CTEs, Relational Joins, ETL Pipelines</li>
</ul>
    </td>
  </tr>
</table>

---

<h2 align="center">Insights Deep-Dive</h2>
<table align="center">
  <tr>
    <td width="1440">

<h3>1. Supplier Dependency & Spend Concentration (Pareto Analysis)</h3>
<ul>
  <li>
    The analysis revealed a strong concentration of procurement spend, where a small group of top vendors accounted for <strong>80%+ of total purchase value</strong>. 
    This indicates high dependency on a limited supplier base, increasing exposure to supply-chain disruptions, pricing power imbalance, and operational risk.
  </li>
  <li>
    The Pareto pattern highlights an opportunity for both <strong>risk mitigation</strong> (vendor diversification) and <strong>strategic negotiation</strong> with high-impact suppliers.
  </li>
</ul>

<h3>2. Pricing Efficiency & Bulk Purchasing Impact</h3>
<ul>
  <li>
    Order-size analysis showed a clear inverse relationship between purchase volume and unit cost. 
    Vendors purchasing in large volumes achieved an average <strong>~72% reduction in unit purchase price</strong> compared to small-volume orders.
  </li>
  <li>
    This confirms that existing bulk pricing strategies are effective, but also highlights untapped opportunities to extend volume-based discounts to medium-tier vendors with stable demand.
  </li>
</ul>

<h3>3. Profit Margin vs Sales Volume Trade-Off</h3>
<ul>
  <li>
    Comparative analysis across vendors showed that <strong>high-sales vendors tend to operate at lower profit margins</strong>, likely due to competitive pricing and volume-driven strategies.
  </li>
  <li>
    Conversely, several low-performing vendors exhibited <strong>higher average profit margins but low sales volume</strong>, indicating potential pricing rigidity or limited market reach rather than poor product economics.
  </li>
</ul>

<h3>4. Inventory Turnover & Capital Lock-In Risk</h3>
<ul>
  <li>
    Vendors with a <strong>stock turnover ratio below 1</strong> were identified as major contributors to unsold inventory value, signaling slow-moving or overstocked products.
  </li>
  <li>
    This unsold inventory represents <strong>significant working capital locked</strong> in non-performing assets, increasing storage costs and reducing cash flow flexibility.
  </li>
</ul>

<h3>5. Statistical Validation of Vendor Performance Differences</h3>
<ul>
  <li>
    A two-sample t-test confirmed a <strong>statistically significant difference (p &lt; 0.05)</strong> between the mean profit margins of top-performing and low-performing vendors.
  </li>
  <li>
    The 95% confidence intervals further showed that low-performing vendors consistently maintained <strong>higher margin ranges</strong>, validating that margin differences were structural rather than random fluctuations.
  </li>
</ul>

  </td>
  </tr>
</table>


---

<h2 align="center">Results & Business Recommendations</h2>
<table align="center">
  <tr>
    <td width="1440">
<h3>📌 Pricing & Growth Optimization</h3>
<ul>
  <li>Re-evaluate pricing for low-sales, high-margin brands to unlock volume growth without sacrificing profitability.</li>
</ul>

<h3>📌 Procurement & Risk Management</h3>
<ul>
  <li>Diversify vendor partnerships to reduce dependency risk and strengthen supply-chain resilience.</li>
  <li>Leverage bulk purchasing advantages to maintain competitive pricing while optimizing inventory levels.</li>
</ul>
    </td>
  </tr>
</table>

---

<h2 align="center">Key Learnings</h2>
<table align="center">
  <tr>
    <td width="1440">
<ul>
  <li>Vendor performance must be evaluated across margin, volume, and inventory efficiency—not sales alone.</li>
  <li>Statistical validation strengthens business confidence in analytical insights.</li>
  <li>Well-modeled BI dashboards translate complex analysis into actionable strategy.</li>
</ul>
    </td>
  </tr>
</table>

---

<h2 align="center">Limitations</h2>

<table align="center">
  <tr>
    <td width="1440">
<ul>
  <li>Analysis is based on historical transactional data and does not account for external market shocks.</li>
  <li>Freight and pricing assumptions depend on available vendor-level granularity.</li>
</ul>
    </td>
  </tr>
</table>

---

<h2 align="center">Next Steps</h2>
<table align="center">
  <tr>
    <td width="1440">
<ul>
  <li>Integrate demand forecasting to optimize reorder quantities.</li>
  <li>Extend supplier scorecards with delivery reliability and quality metrics.</li>
</ul>

  </td>
  </tr>
</table>

---

<h3 align="center">📊 This project demonstrates how data analytics can directly drive procurement efficiency, risk mitigation, and sustainable profitability.</h3>

---

<h2 align="center">Contact</h2>
<table align="center">
  <tr>
    <td align="center" width="1440">
      <p>
        If you’d like to discuss the <strong>code</strong>, the <strong>dashboard</strong>, or the <strong>business insights</strong>,
        feel free to reach out via GitHub or email.
      </p>

  <p>
        📧 <strong>Email:</strong> kaifsdkpro@gmail.com
      </p>

  <p>
        📬 <strong>LinkedIn:</strong>
        <a href="https://www.linkedin.com/in/kaifsayed57/" target="_blank">
          linkedin.com/in/kaifsayed57
        </a>
      </p>

  <p>
        ⭐ <strong>If you found this project insightful, don’t forget to star this repository!</strong>
      </p>

  <p>
        Open to Data Analyst, Business Analyst, and Excel / SQL / Power BI–based analytics roles.
      </p>
  <p>
        <em></em>
      </p>
    </td>
  </tr>
</table>

<h4 align="center"><em>Made with ❤️ — Kaif Anis Sayed</em></h4>
