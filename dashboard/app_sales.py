#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dashboard_building.ipynb

import pandas as pd
import streamlit as st
import plotly.express as px

# Load cleaned dataset
df = pd.read_csv("/Users/Keswickb/Desktop/retail-sales-dashboard/data/processed/retail_sales_clean.csv", parse_dates=['order_date'])

st.title("📊 Retail Sales Dashboard")

# --- Filters ---
region = st.selectbox("Select Region", df["region"].unique())
filtered_df = df[df["region"] == region]

# Sales Over Time
sales_over_time = filtered_df.groupby("order_date")["sales"].sum().reset_index()
fig1 = px.line(sales_over_time, x="order_date", y="sales", title=f"Sales Over Time in {region}")
st.plotly_chart(fig1)

# Sales by Category 
fig2 = px.bar(filtered_df, x="category", y="sales", color="category", title="Sales by Category", barmode="group")
st.plotly_chart(fig2)

# Top Products 
top_products = (
    filtered_df.groupby("product_name")["sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
fig3 = px.bar(top_products, x="product_name", y="sales", title="Top 10 Products")
st.plotly_chart(fig3)

