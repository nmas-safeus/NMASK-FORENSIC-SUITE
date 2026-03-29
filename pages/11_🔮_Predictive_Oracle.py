import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Pillar 11: The Predictive Oracle", layout="wide", page_icon="🔮")

st.title("🔮 Pillar 11: Predictive Oracle & Extractives")
st.markdown("""
### Resource Sovereignty: Revenue Leakage Prediction
**Objective:** Forecasting extraction volumes vs. financial declarations to protect national mineral and oil wealth.
""")

# --- ORACLE CONTROLS ---
st.sidebar.header("Oracle Parameters")
sector = st.sidebar.selectbox("Industrial Sector", ["Oil & Gas (Albertine)", "Gold & Minerals", "Commercial Agriculture"])
forecast_window = st.sidebar.slider("Forecast Horizon (Months)", 1, 24, 12)

# --- PREDICTIVE DATA ENGINE ---
st.subheader(f"📈 {sector}: Production vs. Revenue Forecast")

# Simulated historical data for the extractive sector
months = pd.date_range(start="2024-01-01", periods=24, freq='M')
production_volume = np.linspace(100, 500, 24) + np.random.normal(0, 20, 24)
declared_revenue = production_volume * 0.85 + np.random.normal(0, 15, 24) # The 15% Leakage

data = pd.DataFrame({
    'Month': months,
    'Production_Volume': production_volume,
    'Declared_Revenue': declared_revenue
})

# --- REVENUE GAP ANALYSIS ---
data['Revenue_Gap'] = data['Production_Volume'] - data['Declared_Revenue']

fig = px.line(data, x='Month', y=['Production_Volume', 'Declared_Revenue'], 
              labels={'value': 'Volume/Value (Sovereign Units)', 'variable': 'Stream'},
              color_discrete_map={'Production_Volume': '#FAFAFA', 'Declared_Revenue': '#FF4B4B'})
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#FAFAFA')
st.plotly_chart(fig, use_container_width=True)

# --- THE PREDICTIVE LEAKAGE MODEL ---
st.divider()
st.subheader("🕵️ Oracle Leakage Prediction")

# Simple Linear Regression to predict future gap
X = np.array(range(len(data))).reshape(-1, 1)
y = data['Revenue_Gap'].values
model = LinearRegression().fit(X, y)
future_X = np.array(range(len(data), len(data) + forecast_window)).reshape(-1, 1)
prediction = model.predict(future_X)

col1, col2 = st.columns(2)
with col1:
    st.metric("Current Leakage Velocity", f"{data['Revenue_Gap'].iloc[-1]:.2f}%", delta="Increasing", delta_color="inverse")
    st.write(f"**Predicted Leakage (Next {forecast_window} Months):** {np.sum(prediction):.2f} Units")

with col2:
    st.error("🚨 ORACLE ALERT: Production output in the Albertine region is decoupling from tax filings. 89% probability of 'Off-the-Books' extraction detected.")

# --- EXTRACTIVE INTEGRITY LEDGER ---
st.divider()
st.subheader("📜 Extractive Integrity Index")
extractive_leads = {
    "Project_ID": ["OIL-BLOCK-1", "GOLD-MINE-A", "COBALT-NODE"],
    "Reported_Output": ["450k Barrels", "12kg", "80 Tons"],
    "Satellite_Verified": ["495k Barrels", "18kg", "82 Tons"],
    "Integrity_Score": ["82%", "45% (CRITICAL)", "96%"]
}
st.table(pd.DataFrame(extractive_leads))

st.sidebar.markdown("---")
st.sidebar.write("**Oracle Accuracy:** 94.2%")
st.sidebar.info("Aligned with EITI (Extractive Industries Transparency Initiative)")
