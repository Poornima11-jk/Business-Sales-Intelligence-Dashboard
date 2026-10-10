import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("sale_data.csv")

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Title
st.title("Business Sales Intelligence Dashboard")

# Region Filter
region = st.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if region != "All":
    filtered_df = df[df["Region"] == region]
else:
    filtered_df = df

# Display data
st.subheader("Sales Data")
st.dataframe(filtered_df)

# Metrics
st.subheader("Key Metrics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Sales",
        filtered_df["Sales Amount"].sum()
    )

with col2:
    st.metric(
        "Total Profit",
        filtered_df["Profit"].sum()
    )

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

monthly_sales = filtered_df.groupby(
    filtered_df["Order Date"].dt.month
)["Sales Amount"].sum()

st.line_chart(monthly_sales)

# Category-wise Sales
st.subheader("Category-wise Sales")

category_sales = filtered_df.groupby(
    "Category"
)["Sales Amount"].sum()

st.bar_chart(category_sales)

# Region-wise Sales
st.subheader("Region-wise Sales")

region_sales = filtered_df.groupby(
    "Region"
)["Sales Amount"].sum()

st.bar_chart(region_sales)

# Top Products
st.subheader("Top Selling Products")

top_products = filtered_df.groupby(
    "Product Name"
)["Sales Amount"].sum().sort_values(
    ascending=False
)

st.bar_chart(top_products)

# Summary
st.subheader("Business Insights")

st.write(
    f"Total Sales: {filtered_df['Sales Amount'].sum()}"
)

st.write(
    f"Total Profit: {filtered_df['Profit'].sum()}"
)

st.write(
    f"Best Selling Product: {top_products.idxmax()}"
)