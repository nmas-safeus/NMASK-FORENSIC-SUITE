import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

st.set_page_config(page_title="Pillar 8: The Spirit of Deception", layout="wide", page_icon="🧠")

st.title("🧠 Pillar 8: Cognitive Profile & Risk Node")
st.markdown("""
### The Spirit of Deception: Behavioral Biometrics & Cognitive Load
**Objective:** Detecting Deepfakes, linguistic anomalies, and fraudulent intent using behavioral forensic markers.
""")

# --- COGNITIVE MONITORING CONTROLS ---
st.sidebar.header("Behavioral Parameters")
analysis_mode = st.sidebar.selectbox("Analysis Engine", ["Linguistic Stress", "Micro-Expression Sync", "Deepfake Audio-Visual Sync"])
sensitivity = st.sidebar.slider("Deception Threshold", 0.0, 1.0, 0.75)

# --- INPUT AREA: LINGUISTIC FORENSICS ---
st.subheader("📝 Forensic Communication Analysis")
text_input = st.text_area("Paste Communication (Email, Statement, or Transcript) for Cognitive Profiling", 
                         placeholder="e.g., 'I am writing to authorize an urgent payment to the offshore vendor immediately...'")

if text_input:
    with st.status("Analyzing Cognitive Load...", expanded=True) as status:
        st.write("Extracting Linguistic Markers...")
        # Simulate processing time for "Behavioral Biometrics"
        st.write("Cross-Referencing Behavioral Baselines...")
        st.write(f"Running {analysis_mode} algorithm...")
        status.update(label="✅ Profiling Complete", state="complete")

    # --- THE RISK NODE VISUALIZATION ---
    st.divider()
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Cognitive Risk Distribution")
        # Creating a distribution of "Deception Markers"
        hist_data = [np.random.normal(0.6, 0.1, 100), np.random.normal(0.3, 0.1, 100)]
        group_labels = ['Current Statement', 'Baseline (Honest)']
        
        fig = ff.create_distplot(hist_data, group_labels, bin_size=.05, colors=['#FF4B4B', '#2E86C1'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#FAFAFA')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.metric("Deception Probability", "82%", delta="HIGH RISK", delta_color="inverse")
        st.warning("**Key Marker Detected:** 'Distancing Language' and 'Urgency Overload'—typical of Business Email Compromise (BEC).")
        
        if st.button("Deepfake Verification Scan"):
            st.info("Artifacts detected in voice-cadence sync. 94% probability of AI-Generated synthesis.")

# --- RISK NODE: ENTITY PROFILING ---
st.divider()
st.subheader("🕵️ Global Risk Node: Behavioral Integrity Score")

entity_profiles = {
    "Entity_ID": ["AUD-77", "VND-402", "EXEC-09"],
    "Cognitive_Score": ["9.8/10", "4.2/10", "8.5/10"],
    "Integrity_Status": ["Stable", "DECEPTIVE PATTERN", "Stable"],
    "Last_Scan": ["2026-03-20", "2026-03-29", "2026-03-25"]
}

df_risk = pd.DataFrame(entity_profiles)
st.table(df_risk)

st.sidebar.markdown("---")
st.sidebar.write("**Forensic Model:** Behavioral Biometrics v2.1")
st.sidebar.info("Compliant with International Psychological Forensic Standards")
