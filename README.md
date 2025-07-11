# Financial Clarity Reporting

## Project Description
This project combines a business-facing Power BI e-commerce dashboard with a backend Python-based churn prediction model to deliver actionable insights into customer behavior and retention strategies.

It’s designed as an MVP to help e-commerce operators answer critical questions:
- Who are our best customers?
- When do customers usually reorder?
- Which customers are at risk of churning?
- How are ads performing across platforms?

The goal is to enable smarter marketing, increase customer lifetime value (LTV), and inform re-engagement campaigns — all powered by accessible data tools and predictive analytics.

## Features
📊 Power BI Dashboard
- Revenue & Orders Overview: Track sales, AOV, and order volume over time
- Customer Segmentation: Break down New, Active, and Churned customers
- Reorder Behavior Heatmap: Visualize time until next order
- Ad Spend Analysis: Compare performance by platform (Spend, ROAS, CAC)
- Profitability Snapshot: Real-time margins, net revenue, and LTV

🤖 Churn Prediction Model (Python)
- Labels customers as New, Active, or Churned based on behavior
- Engineers features like AOV, order frequency, days since last order
- Trains a Random Forest classifier to predict churn probability
- Outputs scores for all customers with confidence levels
- Visualizes churn distribution and feature importance

## Project Includes:
1. README.md: Documentation and project guide
2. FitFuel_Company_Supplement_Store.pbix: Fully interactive Power BI file
3. ChurnModelingE-Commerce.ipynb: Jupyter notebook with churn prediction pipeline
4. Predictive_Output.xlsx: churn prediction predictions output file from ChurnModelingE-Commerce 
5. Ecommercedash.png: Image of FitFuel_Company_Supplement_Store.pbix
6. ChurnPredictionsOutput.png: Image of Predictive_Output.xlsx

Data:
1. orders.csv: transaction data - Fact Table
2. ads.csv: ad data - Fact Table
3. customers.csv: Customers data - Dimension Table
4. products.csv: Products data - Dimension Table

## Tech Stack
- Microsoft Power BI
- Python (Pandas, Scikit-learn, Matplotlib)
  
Contact: 
Website: https://www.jakelender.com
Email: Jakelender@gmail.com

## Screenshots
![alt text](https://github.com/JacobLender/Ecommerce-Insights/blob/02d8d76439a9ef80aa0d2985a8a4681dee7e610f/Ecommercedash.png)
![alt text](https://github.com/JacobLender/Ecommerce-Insights/blob/c1b704fd6007e3b7178a70515f1ea7e4d3cad71d/ChurnPredictionsOutput.png)
