import streamlit as st
import joblib

model = joblib.load("Pricepilotaii.pkl")

st.set_page_config(page_title="PricePilot AI")

st.title("✨🚗 PricePilot AI🚗✨")
st.subheader("Car Price Prediction")

st.write("Welcome to PricePilot AI!")
st.write("Predict estimated car prices using Machine Learning.")
