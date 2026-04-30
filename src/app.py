import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- THE TOOLKIT (OOP) ---
class ClimateDashboard:
    def __init__(self, file_path, country):
        self.df = pd.read_csv(file_path)
        self.country = country

    def show_metrics(self):
        # Shows the hottest and rainiest records
        hottest = self.df['T2M'].max()
        rainiest = self.df['PRECTOTCORR'].max()
        col1, col2 = st.columns(2)
        col1.metric("Max Temp", f"{hottest}°C")
        col2.metric("Max Rainfall", f"{rainiest}mm")

    def plot_data(self):
        # Creates the chart for the website
        fig, ax = plt.subplots()
        sns.lineplot(data=self.df, x='YEAR', y='T2M', ax=ax, color='red')
        plt.title(f"Temperature Trend in {self.country}")
        st.pyplot(fig)

# --- THE WEBSITE INTERFACE ---
st.title("🌍 EthioClimate Analytics Dashboard")
st.write("Supporting Ethiopia's data-driven position for COP32.")

# Sidebar for country selection
option = st.sidebar.selectbox(
    'Select a Country to Analyze:',
    ('ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania'))

# Run the analyzer
app = ClimateDashboard(f"{option}.csv", option.capitalize())

st.header(f"Results for {option.capitalize()}")
app.show_metrics()
app.plot_data()

st.divider()
st.header("📋 Negotiation-Grade Summary for COP32")
st.subheader("1. What is changing?")
st.write(f"In {option.capitalize()}, we observe clear temperature cycles with a rising trend in recent years.")

st.subheader("2. What did it cause?")
st.write("Extreme events, like the record rainfall peaks shown in the metrics above, lead to sudden flooding and soil erosion.")

st.subheader("3. What does it demand?")
st.write("We demand climate adaptation finance to build resilient infrastructure against these unpredictable weather shifts.")