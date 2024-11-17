import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import optimize_supply_chain

def run():
    st.header("Supply Chain Optimization Dashboard")
    st.write("Optimize logistics and inventory management with data insights.")

    # Load dataset
    data = pd.read_csv("data/supply_chain_data.csv")
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    # Interactive Visualization
    st.write("### Inventory Trends")
    fig = px.bar(
        data,
        x="product_id",
        y="stock_level",
        color="lead_time",
        title="Stock Levels by Product",
        labels={"product_id": "Product ID", "stock_level": "Stock Level"},
    )
    st.plotly_chart(fig)

    st.write("### Demand vs. Stock Level")
    fig2 = px.scatter(
        data,
        x="demand",
        y="stock_level",
        color="product_id",
        size="lead_time",
        title="Demand vs. Stock Level",
        labels={"demand": "Demand", "stock_level": "Stock Level"}
    )
    st.plotly_chart(fig2)

    # Optimization
    if st.button("Run Optimization"):
        optimized_results = optimize_supply_chain(data)
        st.write("### Optimized Results")
        st.dataframe(optimized_results)
