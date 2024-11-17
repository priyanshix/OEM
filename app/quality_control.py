import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.header("Quality Control Dashboard")
    st.write("Analyze defect data for quality improvement.")

    # Load dataset
    data = pd.read_csv("data/sensor_data.csv")
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    # Placeholder Visualization
    st.write("### Sensor Value Distribution")
    fig = px.histogram(
        data,
        x="value",
        color="sensor_id",
        title="Sensor Value Distribution",
        labels={"value": "Sensor Value"},
        nbins=30
    )
    st.plotly_chart(fig)

    st.info("This module is under development. More features coming soon!")
