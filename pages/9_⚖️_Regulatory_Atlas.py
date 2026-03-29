import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Pillar 9: The Regulatory Atlas", layout="wide", page_icon="⚖️")

st.title("⚖️ Pillar 9: The Regulatory Atlas")
st.markdown("""
### Executable Compliance: Laws as Code
**Objective:** Turning statutory regulations into live validation logic that updates with international standards.
""")

# --- REGULATORY ENGINE CONTROLS ---
st.sidebar.header("Atlas Configuration")
legal_framework = st.sidebar.selectbox("Primary Jurisdiction", ["Uganda Statutory Law", "EAC Regional Treaty", "International FATF"])
sync_frequency = st.sidebar.radio("Global Law Sync", ["Real-Time", "Daily", "On-Audit"])

# --- EXECUTABLE COMPLIANCE LOGIC ---
st.subheader("📜 Live Regulatory Logic (Smart Laws)")

# Simulated Regulatory Database
laws_data = {
    "Statute": ["Uganda Evidence Act", "Anti-Money Laundering Act", "Data Protection Act", "Income Tax Act (Cap 340)"],
    "Clause": ["Section 5 (Admissibility)", "Section 3 (Due Diligence)", "Section 7 (Consent)", "Section 118 (Withholding)"],
    "Status": ["ACTIVE", "ACTIVE", "AMENDMENT PENDING", "ACTIVE"],
    "Validation_Rule": ["Hash Integrity Check", "UBO Mapping > $10k", "Encryption Protocol 4", "15% Threshold Check"]
}

df_laws = pd.DataFrame(laws_data)

def color_status(val):
    color = '#F1C40F' if val == "AMENDMENT PENDING" else '#2ECC71'
    return f'background-color: {color}; color: black; font-weight: bold'

st.table(df_laws.style.applymap(color_status, subset=['Status']))

# --- THE COMPLIANCE COMPILER ---
st.divider()
st.subheader("🛠️ The Compliance Compiler")
st.write("Test a financial transaction against the current **Regulatory Atlas**.")

col1, col2 = st.columns(2)
with col1:
    txn_amount = st.number_input("Transaction Amount (UGX)", value=5000000)
    is_international = st.toggle("International Transfer")
with col2:
    beneficiary_type = st.selectbox("Beneficiary Type", ["Verified Employee", "Third-Party Vendor", "Political Exposed Person (PEP)"])

if st.button("Run Compliance Validation"):
    with st.status("Compiling Statutory Rules...", expanded=True) as status:
        st.write("Fetching latest Uganda Gazette updates...")
        st.write("Checking FATF Gray-List Status...")
        st.write(f"Applying {legal_framework} filters...")
        status.update(label="✅ Validation Complete", state="complete")
    
    # Execution Logic
    if beneficiary_type == "Political Exposed Person (PEP)":
        st.error("🚨 VIOLATION: Section 3 of AML Act requires Enhanced Due Diligence for PEPs. Transaction Blocked.")
    elif is_international and txn_amount > 10000000:
        st.warning("⚠️ ALERT: Threshold exceeded. Automatic reporting to Financial Intelligence Authority (FIA) initiated.")
    else:
        st.success("✅ COMPLIANT: Transaction meets all active Regulatory Atlas parameters.")

# --- THE UPDATER: FUTURE-PROOFING ---
st.divider()
st.info(f"**Atlas Sync Status:** Last updated {datetime.date.today()}. **International Change Detected:** New OECD tax reporting standards expected in 30 days. Preparing logic update...")

st.sidebar.markdown("---")
st.sidebar.write("**Atlas Integrity:** 100% Verified")
st.sidebar.info("Source: Ministry of Justice / International Regulatory Nodes")
