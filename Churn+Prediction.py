# Churn Modeling
# Load order data and label churn

# Import libraries
import pandas as pd 
from datetime import datetime, timedelta 

# Load Order Data
orders = pd.read_csv(r"C:\Users\jakel\OneDrive\Desktop\Money Money Money\Fitness E-Commerce")

print(orders.head())