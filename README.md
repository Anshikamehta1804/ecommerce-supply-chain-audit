

# E-Commerce Supply Chain & Delivery Performance Audit

## 📌 Project Overview
In large-scale e-commerce logistics, delivery delays impact customer retention, inflate customer support overhead, and increase operational expenses. 

This project delivers an end-to-end operational performance audit of **10,999 e-commerce fulfillment orders**. By bridging **Python**, **SQL**, and **Power BI**, the pipeline ingests raw shipping data, identifies logistical bottlenecks across fulfillment nodes, executes predictive risk classification for delivery punctuality, and reports core executive metrics.

---

## 📊 Executive Dashboard Preview

![Power BI Delivery Performance Dashboard](./power_bi_dashboard_preview)

### Key Metrics Tracked:
* **Total Audited Orders:** 10,999 shipments
* **Fleet-wide On-Time Delivery (OTD):** 59.7%
* **Average Order Value:** $210.20
* **Average Promo Discount:** $13.37[cite: 3, 4]
* **Support Contact Escalation:** Orders requiring 6+ customer support calls hit peak delivery delay rates of **48.4%**[cite: 3, 4].

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology | Primary Functionality |
| :--- | :--- | :--- |
| **Data Cleaning & ML** | Python (Pandas, Scikit-Learn) | Exploratory data analysis, categorical encoding, feature scaling, and Random Forest delay prediction. |
| **Database & Auditing** | SQL (MySQL) | Schema definition, aggregations, modal split auditing, and fulfillment center delay risk analysis. |
| **Business Intelligence** | Power BI / DAX | Data modeling, dynamic DAX KPIs, and visual cross-filtering across delivery attributes. |

---

## 📂 Repository File Structure

```text
ecommerce-supply-chain-audit/
│
├── Train.csv                                # Kaggle e-commerce fulfillment dataset (10,999 rows)
├── ecommerce_analysis.py                   # Python pipeline for EDA and Random Forest classification
├── warehouse_queries.sql                   # Production SQL queries for relational performance auditing
├── power_bi_dashboard_specification.md     # Full DAX measures and canvas architecture documentation
├── power_bi_dashboard_preview.png          # Executive visualization report screenshot
└── README.md                               # Project documentation
