/* 1. Main Background and Text - FORCED */
    .stApp {
        background-color: #0E1117 !important;
        color: #FAFAFA !important;
    }

    /* 2. Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }

    /* 3. The "NMASK Red" Header Style */
    h1 {
        color: #FF4B4B !important;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-bottom: 2px solid #FF4B4B;
        padding-bottom: 10px;
        margin-bottom: 25px;
    }

    /* 4. Forensic Alert Boxes */
    .stAlert {
        border-radius: 0px;
        border-left: 5px solid #FF4B4B;
        background-color: #1c1f26;
    }

    /* 5. Metric Card (The Numbers) */
    [data-testid="stMetricValue"] {
        font-family: 'IBM Plex Mono', monospace;
        color: #FF4B4B !important;
    }
    
    /* 6. Buttons */
    .stButton>button {
        border-radius: 0px;
        border: 1px solid #FF4B4B;
        background-color: transparent;
        color: #FAFAFA;
    }
    .stButton>button:hover {
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
# --- NAVIGATION & HEADER ---
st.title("🛡️ NMASK Forensic Sovereign Command Center")
st.markdown("""
### The Unified Forensic Operating System
**Project:** NMASK Forensic Consultancy | **Framework:** The Forensic Dozen Blueprint
""")

st.divider()

# --- EXECUTIVE METRICS ---
# These simulate the integration of all 12 pillars
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Identity Integrity (P2)", value="99.8%", delta="0.2%")
    st.caption("Eradicating Ghosts via Quantum-Safe Hashing")

with col2:
    st.metric(label="Shadow Pipe Detection (P5)", value="Active", delta="No Leakage")
    st.caption("Mapping Illicit Flows & Capital Flight")

with col3:
    st.metric(label="Archive Health (P3)", value="100-Year Sync", delta="Immutable")
    st.caption("Laser-Etched Glass Vault Status")

with col4:
    st.metric(label="Judicial Readiness (P12)", value="94%", delta="+5%")
    st.caption("Court-Ready Evidence Probability")

st.divider()

# --- THE FORENSIC RADAR (INTEGRATION VISUAL) ---
st.subheader("🌐 Global Risk Infrastructure (The 12-Pillar Pulse)")

categories = [
    'Moral Anchor', 'Identity Sovereignty', 'The Vault', 
    'Pulse of Truth', 'Shadow Pipes', 'Bounty Hunter',
    'Satellite Truth', 'Spirit of Deception', 'Smart Law',
    'Ledger Lens', 'Resource Sovereignty', 'Ultimate Verdict'
]

# Risk levels 1 (Safe) to 5 (Critical)
risk_values = [1, 2, 1, 3, 2, 4, 1, 2, 1, 3, 2, 1]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
      r=risk_values,
      theta=categories,
      fill='toself',
      name='Forensic Risk Profile',
      line_color='#FF4B4B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(visible=True, range=[0, 5])
  ),
  showlegend=False,
  height=500
)

st.plotly_chart(fig, use_container_width=True)

# --- SYSTEM STATUS ---
st.sidebar.image("https://via.placeholder.com/150?text=NMASK+LOGO", use_container_width=True)
st.sidebar.title("System Integrity")
st.sidebar.success("Quantum Shield: ACTIVE")
st.sidebar.info("Location Scope: Uganda / EAC")
st.sidebar.warning("Evidence Standard: Uganda Evidence Act Compliant")

st.info("💡 **Auditor Note:** Select a specific Pillar from the sidebar to dive into deep-technical forensics.")
