import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pillar 5: Shadow Pipe Detection", layout="wide", page_icon="💸")

st.title("💸 Pillar 5: Illicit Flows & Capital Flight")
st.markdown("""
### Shadow Pipe Detection: Mapping the Global Leakage
**Objective:** Identifying cross-border laundering, TBML, and illicit capital flight in real-time.
""")

# --- GLOBAL MONITORING CONTROLS ---
st.sidebar.header("Shadow Pipe Parameters")
jurisdiction_risk = st.sidebar.multiselect("High-Risk Jurisdictions", ["Offshore Hubs", "Non-Cooperative Territories", "Gray List Zones"], default="Offshore Hubs")
alert_threshold = st.sidebar.slider("Transaction Aggregation Limit (USD)", 1000, 100000, 10000)

# --- FLOW VISUALIZATION (SHADOW PIPES) ---
st.subheader("🌐 Global Flow Analysis: The Shadow Pipe Map")

# Simulated Data for Shadow Pipes
flow_data = pd.DataFrame({
    'Source': ['Uganda', 'Uganda', 'Transit Hub', 'Transit Hub', 'Uganda'],
    'Destination': ['Transit Hub', 'Offshore Hub', 'Tax Haven A', 'Tax Haven B', 'Shadow Shell'],
    'Volume_USD': [500000, 1200000, 450000, 750000, 2100000],
    'Risk_Level': ['Medium', 'High', 'Critical', 'Critical', 'High']
})

fig = px.sunburst(flow_data, path=['Source', 'Destination', 'Risk_Level'], values='Volume_USD',
                  color='Risk_Level', color_discrete_map={'Medium':'#F1C40F', 'High':'#E67E22', 'Critical':'#E74C3C'})
st.plotly_chart(fig, use_container_width=True)

# --- NETWORK MAPPING: TBML DETECTION ---
st.divider()
st.subheader("🕸️ Trade-Based Money Laundering (TBML) Network")
st.caption("Visualizing indirect links between vendors, shell companies, and offshore beneficiaries.")

# Simple NetworkX Simulation
G = nx.Graph()
G.add_edge("Vendor_A", "Logistics_Co")
G.add_edge("Logistics_Co", "Offshore_Beneficiary")
G.add_edge("Vendor_A", "Shadow_Entity_X")
G.add_edge("Shadow_Entity_X", "Offshore_Beneficiary")

fig_net, ax = plt.subplots(figsize=(8, 4))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='#FF4B4B', edge_color='#FAFAFA', font_color='#FAFAFA', font_size=10, ax=ax)
fig_net.patch.set_facecolor('#0E1117')
st.pyplot(fig_net)

# --- FORENSIC ALERTS: CAPITAL FLIGHT ---
st.divider()
st.subheader("🚨 Shadow Pipe Alerts")

alerts = [
    {"Entity": "Agro-Export Corp", "Detection": "Over-Invoicing (TBML)", "Destination": "Mauritius", "Amount": "$850,000"},
    {"Entity": "Unknown Node 7", "Detection": "Layered Smurfing", "Destination": "Cayman Islands", "Amount": "$2,100,000"}
]

for alert in alerts:
    with st.expander(f"🚩 FLAG: {alert['Entity']} - {alert['Amount']}"):
        st.write(f"**Methodology:** {alert['Detection']}")
        st.write(f"**Final Destination:** {alert['Destination']}")
        st.error("Protocol 5 Recommendation: Freeze all linked accounts and initiate Mutual Legal Assistance (MLA).")

# --- SOVEREIGN RECOVERY OVERVIEW ---
st.sidebar.markdown("---")
st.sidebar.write("**Total Detected Leakage:** $3,400,000")
st.sidebar.write("**Status:** Mapping Active Pipes")
st.sidebar.info("Aligned with FATF International Standards")
