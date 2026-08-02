# Retail Sales Analysis 📊

An end-to-end retail sales analysis project — from raw, messy data to business 
insights — built across four tools: **Excel**, **SQL**, **Power BI**, and **Python**.

## 🎯 Project Objective

A retail company needed visibility into which regions, categories, and products 
were actually driving *profit*, not just revenue. This project analyzes 1,000 
order-level transactions to uncover where the business is genuinely profitable, 
where it isn't, and what's driving the difference.

## 🗂️ Repository Structure

```
Retail-Sales-Analysis/
├── data/            # Raw and cleaned datasets
├── excel/           # Pivot tables, KPI formulas, executive summary
├── sql/             # Table setup, data import, and analysis queries
├── powerbi/         # Interactive Power BI dashboard (.pbix)
├── python/          # Data cleaning, KPI analysis, and chart generation
├── report/          # Full business report (PDF + source)
├── screenshots/      # Dashboard and chart images
```

## 🧹 Data Cleaning Challenges

The raw dataset had a few real-world data quality issues, handled consistently 
across every tool in this project:
- `sales` column had comma-formatted values (e.g. `"1,244"`) needing conversion to numeric
- Order/ship dates arrived in **two mixed formats** (`M/D/YYYY` and `DD-MM-YYYY`) in the same column
- International city names required UTF-8 encoding to display correctly

## 📈 Key Results

| Metric | Value |
|---|---|
| Total Revenue | $262,795.00 |
| Total Profit | $29,562.37 |
| Profit Margin | 11.2% |
| Total Orders | 987 |
| Total Customers | 556 |
| Avg. Order Value | $266.26 |

*Validated independently across Excel, SQL, Power BI, and Python — all four produced identical results.*

## 🔍 Key Insights

- **Central region** leads in revenue, but **Africa** converts sales to profit most efficiently.
- **Southeast Asia** is the only region operating at a net loss.
- **Furniture** generates nearly as much revenue as Office Supplies, but a fraction of the profit — driven almost entirely by the **Tables** sub-category, which loses money outright.
- Discounts above **20%** push average profit negative; 0–10% is the healthiest range.

Full analysis and recommendations: [`report/Business_Report.pdf`](report/Business_Report.pdf)

## 🛠️ Tools & Techniques

- **Excel** — Pivot tables, KPI formulas, executive summary
- **SQL (MySQL)** — Aggregate queries, CTEs, window functions (`RANK()`, `LAG()`, `LEAD()`, running totals)
- **Power BI** — DAX measures, cross-filtered dashboard, synced slicers across pages
- **Python (pandas, matplotlib)** — Data cleaning, KPI calculation, chart generation

## 📸 Dashboard Preview

![Power BI Dashboard](screenshots/PowerBI.png)

## 🚀 How to Explore

- **Excel**: open `excel/SuperStoreOrdersfi_cleaned_EDA.xlsx`
- **SQL**: run scripts in `sql/Retail_Sales_Analysis.sql` against a MySQL instance
- **Power BI**: open `powerbi/Retail Sales Dashboard.pbix` in Power BI Desktop
- **Python**: 
```bash
  cd python
  pip install pandas matplotlib
  python retail_sales_analysis.py
```

## 👤 Author

**Lukesh M**
