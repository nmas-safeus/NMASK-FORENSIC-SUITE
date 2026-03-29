import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="NMASK Sovereign Command",
    page_icon="🛡️",
    layout="wide"
)

# 2. Sovereign Branding (CSS Injection)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117 !important; color: #FAFAFA !important; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 1px solid #30363D; }
    h1 { color: #FF4B4B !important; font-family: 'Courier New', Courier, monospace; text-transform: uppercase; border-bottom: 2px solid #FF4B4B; }
    [data-testid="stMetricValue"] { color: #FF4B4B !important; font-family: 'IBM Plex Mono', monospace; }
    .stButton>button { border-radius: 0px !important; border: 1px solid #FF4B4B !important; background-color: transparent !important; color: #FAFAFA !important; }
    .stButton>button:hover { background-color: #FF4B4B !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Header
st.sidebar.markdown("<h1 style='text-align: center;'>NMASK</h1>", unsafe_allow_html=True)
st.sidebar.info("Sovereign Forensic Engine v3.0")

# 4. Main Dashboard Header
st.title("🛡️ NMASK Sovereign Command Center")
st.markdown("### The Unified Forensic Operating System | Project: NMASK Forensic Consultancy")

# 5. Executive Metrics
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Identity Integrity", "99.8%", "+0.2%")
with col2: st.metric("Shadow Pipes", "Active", "No Leakage")
with col3: st.metric("Archive Health", "Synced", "Immutable")
with col4: st.metric("Judicial Readiness", "94%", "Verified")

st.divider()

# 6. The 12-Pillar Radar Chart
st.subheader("🌐 Global Risk Infrastructure (The 12-Pillar Pulse)")

categories = [
    'Master Audit', 'Payroll Identity', 'Digital Forensics', 
    'Synth Audit', 'Illicit Flows', 'Asset Necromancy',
    'Geospatial', 'Cognitive Profile', 'Regulatory Atlas', 
    'Ledger Lens', 'Predictive Oracle', 'Judicial Engine'
]
risk_values = [1, 2, 1, 3, 2, 4, 1, 2, 1, 3, 2, 1]

fig = go.Figure(data=go.Scatterpolar(r=risk_values, theta=categories, fill='toself', line_color='#FF4B4B'))
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 5], gridcolor="#30363D")),
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#FAFAFA', showlegend=False
)
st.plotly_chart(fig, use_container_width=True)

st.success("💡 Select a specific Pillar from the sidebar to begin deep-technical forensics.")
