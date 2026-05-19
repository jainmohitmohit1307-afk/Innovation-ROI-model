# 📊 Innovation ROI & Feasibility Model (Monte Carlo Simulation)

A dynamic, stochastic financial modeling tool designed for Corporate Finance teams, CFOs, and Strategy Directors to rigorously evaluate the ROI of digital transformation and innovation initiatives.

Built with Python and Streamlit, this application replaces fragile, single-point spreadsheet estimates with a robust Monte Carlo simulation, providing a clear, risk-adjusted mathematical probability of project success.

## 🎯 The Problem
Traditional corporate finance models often fail when applied to innovation management because they rely on static estimates. Technology implementations, R&D projects, and digital overhauls carry inherent uncertainty—timelines stretch, budgets overrun, and adoption curves vary.

## 💡 The Solution
This tool runs 10,000 unique financial scenarios using randomized inputs based on custom volatility parameters. It outputs a defensible risk profile, calculating the exact probability that an innovation initiative will achieve a positive Net Present Value (NPV).

### Core Features
* **Stochastic Inputs:** Adjust the mean and volatility (risk percentage) for Capital Expenditure (CapEx), Operating Expenditure (OpEx), and expected Revenue/Value creation.
* **Realistic Adoption Curves:** Automatically scales projected productivity gains over the first 3 years to mimic real-world software/tech adoption.
* **Institutional-Grade Metrics:** Calculates straight-line depreciation, applies corporate tax shields, and discounts cash flows using the firm's Weighted Average Cost of Capital (WACC).
* **Interactive Dashboard:** Real-time data visualization via a Streamlit web interface, including a clean histogram of the simulated NPV distribution.

## 🛠️ Tech Stack
* **Engine:** Python, NumPy, Pandas
* **Visualization:** Matplotlib
* **Web Framework:** Streamlit

## 🚀 Live Demo
This application is deployed live via Streamlit Community Cloud. 
*(You can add your live Streamlit link here once deployed)*

## 💼 Use Cases
Ideal for assessing the financial feasibility of:
* Enterprise software migrations and cloud infrastructure upgrades.
* Launching new digital service lines or corporate spin-offs.
* Broad operational restructuring and R&D capital allocation.
