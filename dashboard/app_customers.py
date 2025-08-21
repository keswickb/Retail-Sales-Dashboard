import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(
        "/Users/keswickb/desktop/retail-sales-dashboard/data/processed/retail_sales_clean.csv"
        # , parse_dates=["order_date"]  # 👈 change this if your column is named differently
    )
    return df

df = load_data()

# Show raw data
st.title("Customer Insights Dashboard")
st.subheader("Retail Customers Dataset Preview")
st.dataframe(df.head())

# Customer Distribution
st.subheader("Customer Distribution")
if "customer_id" in df.columns:
    customer_counts = df["customer_id"].value_counts().reset_index()
    customer_counts.columns = ["customer_id", "transactions"]

    fig = px.histogram(customer_counts, x="transactions", nbins=30, title="Transactions per Customer")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No 'customer_id' column found in dataset.")

# Customer Revenue
st.subheader("Revenue by Customer")
if "customer_id" in df.columns and "sales" in df.columns:
    revenue_per_customer = df.groupby("customer_id")["sales"].sum().reset_index()
    fig2 = px.bar(
        revenue_per_customer.sort_values("sales", ascending=False).head(20),
        x="customer_id",
        y="sales",
        title="Top 20 Customers by Revenue"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No 'customer_id' or 'sales' column found in dataset.")
