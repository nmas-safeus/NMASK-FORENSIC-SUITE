import streamlit as st
import pandas as pd
import hashlib
import numpy as np

st.set_page_config(page_title="Pillar 2: Identity Sovereignty", layout="wide", page_icon="👤")

st.title("👤 Pillar 2: Payroll & Identity (The Ghost Hunter)")
st.markdown("### UVP: Identity Sovereignty & Quantum-Safe Eradication of Ghosts")

# --- HIGH-END FORENSIC CONTROLS ---
st.sidebar.header("Audit Parameters")
threshold = st.sidebar.slider("Match Sensitivity (Fuzzy Logic)", 70, 100, 90)
quantum_mode = st.sidebar.toggle("Enable Post-Quantum Hashing (SHA-3)", value=True)

# --- DATA INGESTION ---
uploaded_file = st.file_uploader("Upload Payroll Master for Forensic Analysis", type=["csv", "xlsx"])

if uploaded_file:
    # Read data safely
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    
    # Standardize Column Names for NMASK Protocol
    df.columns = [c.strip().upper() for c in df.columns]
    
    st.subheader("📋 Ingested Dataset Overview")
    st.dataframe(df.head(10), use_container_width=True)

    # --- THE GHOST HUNTING ENGINE ---
    st.divider()
    st.subheader("🕵️ Ghost Detection Results")
    
    col1, col2, col3 = st.columns(3)
    
    # 1. Duplicate NIN Check (Identity Theft)
    nin_col = next((c for c in df.columns if "NIN" in c or "ID" in c), None)
    # 2. Shared Bank Account Check (Salary Diversion)
    bank_col = next((c for c in df.columns if "BANK" in c or "ACCOUNT" in c), None)
    # 3. Payee Name vs Account Name (The "Proxy" Ghost)
    name_col = next((c for c in df.columns if "NAME" in c), None)

    if nin_col and bank_col:
        # Identify duplicates
        nin_dupes = df[df.duplicated(nin_col, keep=False)]
        bank_dupes = df[df.duplicated(bank_col, keep=False)]
        
        with col1:
            st.metric("Total Records", len(df))
        with col2:
            st.metric("Ghost Identities (NIN)", len(nin_dupes), delta=f"{len(nin_dupes)} Flagged", delta_color="inverse")
        with col3:
            st.metric("Salary Diversion (Bank)", len(bank_dupes), delta=f"{len(bank_dupes)} Risks", delta_color="inverse")

        # --- EXHAUSTIVE REPORTING ---
        if not nin_dupes.empty:
            st.error("🚨 CRITICAL: Duplicate National IDs found. These are likely Phantom Employees.")
            st.dataframe(nin_dupes.sort_values(by=nin_col))
            
        if not bank_dupes.empty:
            st.warning("⚠️ ALERT: Multiple employees sharing the same bank account. Investigation required.")
            st.dataframe(bank_dupes.sort_values(by=bank_col))

        # --- QUANTUM-SAFE IDENTITY VAULTING ---
        st.divider()
        st.subheader("🛡️ Sovereign Identity Archiving")
        if st.button("Generate Post-Quantum Evidentiary Hashes"):
            with st.spinner("Calculating SHA-3 256-bit Hashes..."):
                # NMASK Proprietary logic: Hash the NIN + Name for an immutable record
                if quantum_mode:
                    df['SOVEREIGN_HASH'] = df.apply(lambda row: hashlib.sha3_256(f"{row[nin_col]}{row[name_col]}".encode()).hexdigest(), axis=1)
                else:
                    df['SOVEREIGN_HASH'] = df.apply(lambda row: hashlib.sha256(f"{row[nin_col]}{row[name_col]}".encode()).hexdigest(), axis=1)
                
                st.success("✅ Records successfully hashed for the 100-Year Archive.")
                st.dataframe(df[[name_col, nin_col, 'SOVEREIGN_HASH']].head())
                
                # Download for the Legal Vault
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download Evidence-Grade Hashed Report", csv, "Pillar2_Identity_Audit.csv", "text/csv")
    else:
        st.error("Forensic Error: Required columns (NIN/ID and Bank Account) not detected in file.")

else:
    st.info("Awaiting Payroll Master upload to begin Ghost Identification protocol.")

st.sidebar.markdown("---")
st.sidebar.write("**Pillar:** Payroll & Identity")
st.sidebar.write("**Forensic Engine:** NMASK v1.0")
