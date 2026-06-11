import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. SYSTEM CONFIGURATION & GLOBAL DESIGN
# ---------------------------------------------------------
st.set_page_config(page_title="Drake National Resilience Engine", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stApp { background-color: #050505; }
    .card { background-color: #121212; padding: 20px; border-radius: 8px; border: 1px solid #333; margin-bottom: 10px; }
    .header-text { color: #007bff; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ National Resilience Engine: Integrated Systemic Attrition Model (2026)")

# ---------------------------------------------------------
# 2. GLOBAL CONTROL DECK (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    st.header("🕹️ Master Control Deck")
    # 1. Macro Global Toggle (6-Stage Escalation Ladder)
    escalation_stage = st.select_slider("Macro-Escalation Ladder", options=[1, 2, 3, 4, 5, 6], value=1)
    
    # 5. Long-Term Temporal Engine
    temporal_runway = st.selectbox("Temporal Runway", ["2025-2035 Active Planning", "2035-2050 Closure Corridor"])
    
    st.markdown("---")
    st.header("⚡ Strategic Policy Panel")
    # 7. Binary Mitigation Switches
    emp_hard = st.checkbox("EMP Hardening Enabled")
    maritime_audit = st.checkbox("Maritime UBO Audits")
    academic_firewall = st.checkbox("Academic Funding Firewalls")
    def_realloc = st.checkbox("Strategic Defense Reallocations")

# ---------------------------------------------------------
# 3. TAB ARCHITECTURE & CORE MODULES
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📊 Quant Core", "⚓ Logistics & LNG", "🏛️ Silicon Shield & C2", "🚨 Asymmetric Risks"])

# --- TAB 1: QUANT CORE ---
with tab1:
    st.subheader("Global System State Diagnostic")
    st.metric("Systemic Integrity Score", f"{100 - (escalation_stage * 12)}%", delta=f"-{escalation_stage * 5}% Daily Decay")
    
    # Cascade Logic
    if escalation_stage >= 4:
        st.error("⚠️ SYSTEM CRITICAL: Kinetic Flashpoint Threshold Exceeded.")
    else:
        st.success("🟢 System Stable: Operational Runway Intact.")

# --- TAB 2: LOGISTICS & LNG CASCADE ---
with tab2:
    st.subheader("⚓ Infrastructure Node Timelines")
    col1, col2 = st.columns(2)
    with col1:
        st.info("### Logistics: Kaohsiung Throughput")
        # 2. Logistics Cascade (T+0 to T+11)
        st.progress(max(1.0 - (escalation_stage * 0.15), 0.05))
        st.write("T+11 Day Collapse threshold active.")
    with col2:
        st.info("### LNG Grid Compression")
        # 2. LNG Grid Compression Phases
        lng_status = st.slider("Manifold Stability", 0, 100, 100 - (escalation_stage * 15))
        st.write("Pressure degradation accelerating.")

# --- TAB 3: SILICON SHIELD & C2 ---
with tab3:
    st.subheader("🏛️ Silicon Shield & C2 Health")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("#### Chemical Buffer (Gas Stockpiles)")
        st.slider("Neon/Helium Runway (Days)", 0, 90, 30 - (escalation_stage * 4))
    with col_b:
        st.write("#### 5-Layer C2 Communications Failover")
        layers = ["LEO Satellites", "HARS", "Troposcatter", "Hardened Terrestrial", "HF/VHF/UHF"]
        for layer in layers:
            st.checkbox(layer, value=True if escalation_stage < 3 else False)

# --- TAB 4: ASYMMETRIC THREATS & LICENSING ---
with tab4:
    st.subheader("🚨 Asymmetric Threat Coordinates")
    # 3. Sleeper Operation Scenarios
    threat_data = pd.DataFrame({
        "Operation": ["Qixingtan Spark", "Subsea Interdiction", "Tech-Leakage", "Grid-Sync", "Data-Flood", "Bank-Run", "Trade-Freeze"],
        "Probability": [0.45, 0.62, 0.81, 0.55, 0.70, 0.40, 0.88],
        "Impact": [0.95, 0.85, 0.60, 0.75, 0.65, 0.90, 0.99]
    })
    st.dataframe(threat_data, use_container_width=True)
    
    st.markdown("---")
    # 8. Institutional Licensing Portal
    st.warning("💰 **Institutional Access Restricted**")
    st.markdown("This model is currently licensed for sovereign risk assessment. To unlock the full *Taiwan Black Box Series*, contact the Drake Institute for institutional credentials.")

# ---------------------------------------------------------
# 4. FINAL SYSTEM FOOTER
# ---------------------------------------------------------
st.markdown("---")
st.caption(f"Engine Status: {temporal_runway} | Resilience Engine v2.06 | Confidentiality Tier: Sovereign")
