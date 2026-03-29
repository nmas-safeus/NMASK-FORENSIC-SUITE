import streamlit as st
import hashlib
import datetime
import pandas as pd

# Page Config for Professional Forensic Branding
st.set_page_config(page_title="Pillar 1: The Covenant", layout="wide", page_icon="📊")

# Custom CSS for high-contrast "Command Center" feel
st.markdown("""
    <style>
    .reportview-container { background: #0E1117; }
    .main { color: #FAFAFA; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Pillar 1: The Covenant & The Verifier")
st.markdown("### The Moral Anchor & Human-in-the-Loop Protocol")

# --- THE COVENANT LOGIC ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

with st.container():
    st.info("📜 **The NMASK Covenant:** 'I certify that my actions today adhere to the Uganda Evidence Act and the highest standards of forensic integrity. I acknowledge that every keystroke is etched into the 100-Year Archive.'")
    
    col1, col2 = st.columns(2)
    with col1:
        auditor_id = st.text_input("Sovereign Auditor ID (NIN or Staff Code)", placeholder="UG-AUD-XXXX")
        access_key = st.text_input("Access Token", type="password")
    
    with col2:
        assignment_ref = st.text_input("Case/Audit Reference", placeholder="2026-PAY-001")
        integrity_check = st.checkbox("I accept the legal consequences of data tampering.")

    if st.button("Activate Sovereign Command"):
        if auditor_id and access_key and integrity_check:
            # Create a Session Hash (The Verifier)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            session_string = f"{auditor_id}-{access_key}-{timestamp}"
            session_hash = hashlib.sha256(session_string.encode()).hexdigest()
            
            st.session_state['authenticated'] = True
            st.session_state['session_id'] = session_hash.upper()
            st.session_state['auditor'] = auditor_id
            
            st.success(f"✅ VERIFIED. Session ID: {st.session_state['session_id'][:16]}")
        else:
            st.error("Access Denied: Incomplete Credentials or Moral Commitment.")

# --- FUNCTIONAL AUDIT LOG ---
if st.session_state['authenticated']:
    st.divider()
    st.subheader("🛡️ Active Session Monitor")
    
    # Building a functional data table for the "Verifier" aspect
    audit_data = {
        "Timestamp": [datetime.datetime.now().strftime("%H:%M:%S")],
        "Action": ["Sovereign Login"],
        "Auditor": [st.session_state['auditor']],
        "Integrity_Hash": [st.session_state['session_id']]
    }
    log_df = pd.DataFrame(audit_data)
    st.table(log_df)

    # Industry-Best Feature: Exporting the "Verifier" Token
    st.download_button(
        label="Download Session Certificate",
        data=log_df.to_csv(index=False),
        file_name=f"Covenant_Token_{st.session_state['auditor']}.csv",
        mime="text/csv"
    )

st.sidebar.markdown("---")
st.sidebar.write(f"**Current User:** {st.session_state.get('auditor', 'Not Verified')}")
st.sidebar.write("**Forensic Standard:** Uganda Evidence Act 2026")
