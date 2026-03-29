import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go

st.set_page_config(page_title="Pillar 4: Synth-Audit", layout="wide", page_icon="🩺")

st.title("🩺 Pillar 4: Synth-Audit & Monitoring")
st.markdown("""
### The Pulse of Truth: Real-Time Ingestion & Fraud Interception
**Objective:** Detecting synthetic anomalies and fraudulent velocity *before* the financial settlement occurs.
""")

# --- REAL-TIME MONITORING CONTROLS ---
st.sidebar.header("Monitoring Sensitivity")
ingestion_rate = st.sidebar.select_slider("Data Ingestion Frequency", options=["1s", "5s", "30s", "1m"], value="5s")
anomaly_threshold = st.sidebar.slider("Anomaly Detection Sensitivity", 0.0, 1.0, 0.85)

# --- LIVE DASHBOARD ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Live Ingestion Stream", "CONNECTED", delta="1024 packets/sec")
with col2:
    st.metric("Processed Transactions", "14,205", delta="+12 since last refresh")
with col3:
    st.metric("Intercepted Risks", "3", delta="-1", delta_color="inverse")

st.divider()

# --- THE "PULSE" VISUALIZATION ---
st.subheader("🌐 The Pulse of Truth: Real-Time Transaction Velocity")

# Simulated live data stream for the 'Pulse'
if "pulse_data" not in st.session_state:
    st.session_state.pulse_data = np.random.randn(50).cumsum()

# Update simulation
new_val = st.session_state.pulse_data[-1] + np.random.randn()
st.session_state.pulse_data = np.append(st.session_state.pulse_data[1:], new_val)

fig = go.Figure()
fig.add_trace(go.Scatter(y=st.session_state.pulse_data, mode='lines', line=dict(color='#FF4B4B', width=2)))
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=300,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=True, zeroline=False),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
st.plotly_chart(fig, use_container_width=True)

# --- SYNTH-AUDIT LOGIC ---
st.subheader("🕵️ Live Synthetic Anomaly Detection")

# Simulated "Pre-Clearance" Interception
transaction_data = {
    "Transaction_ID": ["TXN-9901", "TXN-9902", "TXN-9903"],
    "Entity": ["Global Logistics Ltd", "Shadow Shell Co.", "Verified Vendor A"],
    "Amount_UGX": ["45,000,000", "120,000,000", "12,500,000"],
    "Risk_Score": [0.12, 0.94, 0.05],
    "Status": ["CLEARED", "INTERCEPTED", "CLEARED"]
}

txn_df = pd.DataFrame(transaction_data)

def highlight_risks(val):
    color = 'red' if val == "INTERCEPTED" else 'green'
    return f'color: {color}'

st.table(txn_df.style.applymap(highlight_risks, subset=['Status']))

# --- INTERCEPTION PROTOCOL ---
st.divider()
with st.expander("🛠️ Forensic Interception Protocol"):
    st.write("""
    - **Velocity Check:** Detects if multiple high-value transactions are hitting the same node within seconds.
    - **Synthetic Validation:** Cross-references the 'Pulse' against historical behavioral baselines.
    - **Immediate Freeze:** Intercepted transactions are held in a 'Digital Stasis' until Pillar 12 verification.
    """)

if st.button("Manual System Override / Freeze All"):
    st.error("🚨 GLOBAL FREEZE INITIATED. All outbound payroll transactions suspended for manual review.")

st.sidebar.markdown("---")
st.sidebar.write("**Pillar:** Synth-Audit & Monitoring")
st.sidebar.write("**Latency:** < 50ms")
