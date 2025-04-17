import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Stock Price Prediction")

# Load saved data
real_prices = np.load("real_prices.npy")
predicted_prices = np.load("predicted_prices.npy")

# Plot actual vs predicted
st.subheader("Predicted vs Actual Prices")

fig, ax = plt.subplots()
ax.plot(real_prices, label='Actual')
ax.plot(predicted_prices, label='Predicted')
ax.legend()
st.pyplot(fig)
