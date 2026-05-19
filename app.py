import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ==========================================
# 1. STREAMLIT UI SETUP (THE DASHBOARD)
# ==========================================
st.set_page_config(page_title="Innovation ROI Calculator", layout="wide")
st.title("📊 Innovation ROI & Feasibility Model")
st.markdown("Quantify the exact mathematical probability of project success before allocating capital.")
st.divider()

# Sidebar for Client Inputs
st.sidebar.header("Project Assumptions")
years = st.sidebar.slider("Project Horizon (Years)", 1, 10, 5)
wacc = st.sidebar.slider("Cost of Capital (WACC %)", 1.0, 30.0, 12.0) / 100
tax_rate = st.sidebar.slider("Corporate Tax Rate (%)", 0.0, 50.0, 30.0) / 100

st.sidebar.subheader("Capital Expenditure (CapEx)")
capex_mean = st.sidebar.number_input("Base Initial CapEx ($)", value=500000, step=50000)
capex_vol = st.sidebar.slider("CapEx Risk / Cost Overrun (%)", 0, 50, 10) / 100

st.sidebar.subheader("Value Creation (Annual)")
rev_mean = st.sidebar.number_input("Expected Annual Value ($)", value=250000, step=25000)
rev_vol = st.sidebar.slider("Value Volatility (%)", 0, 50, 16) / 100

st.sidebar.subheader("Ongoing Costs (OpEx)")
opex_mean = st.sidebar.number_input("Base Annual OpEx ($)", value=50000, step=10000)
opex_vol = st.sidebar.slider("OpEx Risk (%)", 0, 50, 20) / 100

# ==========================================
# 2. MONTE CARLO ENGINE
# ==========================================
iterations = 10000      
adoption_curve = np.array([0.50, 0.80] + [1.00] * (years - 2 if years > 2 else 0))[:years]

np.random.seed(42) 
capex = np.random.normal(capex_mean, capex_mean * capex_vol, iterations)
annual_rev_gain = np.random.normal(rev_mean, rev_mean * rev_vol, iterations)
annual_opex = np.random.normal(opex_mean, opex_mean * opex_vol, iterations)

depreciation = capex / years
npv = -capex.copy()

for t in range(1, years + 1):
    realized_rev = annual_rev_gain * adoption_curve[t-1]
    ebit_t = realized_rev - annual_opex - depreciation
    nopat_t = ebit_t * (1 - tax_rate)
    fcf_t = nopat_t + depreciation
    npv += fcf_t / ((1 + wacc) ** t)

# ==========================================
# 3. AGGREGATE RESULTS
# ==========================================
mean_npv = np.mean(npv)
prob_success = np.sum(npv > 0) / iterations * 100

col1, col2 = st.columns(2)
col1.metric("Expected Mean NPV", f"${mean_npv:,.0f}")
col2.metric("Probability of Positive ROI", f"{prob_success:.1f}%")

st.divider()

# ==========================================
# 4. VISUALIZATION
# ==========================================
st.subheader("Distribution of Project NPV (10,000 Scenarios)")
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(npv, bins=50, color='#2c3e50', edgecolor='white', alpha=0.8)
ax.axvline(x=0, color='#e74c3c', linestyle='--', linewidth=2, label='Break-Even ($0 NPV)')
ax.axvline(x=mean_npv, color='#27ae60', linestyle='-', linewidth=2, label=f'Mean NPV (${mean_npv:,.0f})')
ax.set_xlabel('Net Present Value ($)', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.legend(frameon=True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

st.pyplot(fig)
