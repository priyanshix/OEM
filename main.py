# import streamlit as st
# import pandas as pd
# st.title('OEM Operations AI/ML Dashboard')
# st.write('This is the dashboard for predictive maintenance and other OEM operations features.')
import streamlit as st
from app import predictive_maintenance, quality_control, supply_chain

st.title("OEM AI Platform")
st.sidebar.title("Select a Module")

module = st.sidebar.radio(
    "Choose a module:",
    ("Predictive Maintenance", "Quality Control", "Supply Chain Optimization")
)

if module == "Predictive Maintenance":
    predictive_maintenance.run()
elif module == "Quality Control":
    quality_control.run()
else:
    supply_chain.run()
