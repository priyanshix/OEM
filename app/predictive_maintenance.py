import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import train_predictive_model

def run():
    st.header("Predictive Maintenance Dashboard")
    st.write("Analyze machinery data to predict failures and explore trends.")

    # Load dataset
    data = pd.read_csv("data/sensor_data.csv")
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    # Interactive Visualization
    st.write("### Sensor Data Trends")
    fig = px.line(
        data,
        x="timestamp",
        y="value",
        color="sensor_id",
        title="Sensor Value Trends",
        labels={"value": "Sensor Value", "timestamp": "Time"}
    )
    st.plotly_chart(fig)

    st.write("### Failure Distribution")
    failure_count = data["failure"].value_counts().reset_index()
    failure_count.columns = ["Failure Status", "Count"]
    fig2 = px.pie(
        failure_count,
        names="Failure Status",
        values="Count",
        title="Failure vs. No Failure",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig2)

    # Train the model
    if st.button("Train Model"):
        accuracy = train_predictive_model(data)
        st.success(f"Model trained with accuracy: {accuracy:.2f}")
