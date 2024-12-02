import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Suppress TensorFlow oneDNN warnings

import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler

# Set page configuration
st.set_page_config(layout="wide")

# Custom CSS for grey background and white text
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://miro.medium.com/v2/resize:fit:626/0*SaNg8uUaKCMQSS5g.jpg");
        background-size: cover;
    }
    .white-text {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='white-text'>📈 Stock Price Predictor</h1>", unsafe_allow_html=True)

# Custom label for the multiselect widget
stocks = st.multiselect("Select Stocks", ["GOOG", "AAPL", "MSFT", "AMZN"], label_visibility="collapsed")

# Set date range
end = datetime.now()
start = datetime(end.year - 20, end.month, end.day)

# Dictionary to store stock data
stock_data = {}

# Download stock data for each selected stock
for stock in stocks:
    stock_data[stock] = yf.download(stock, start, end)

# The rest of your script remains unchanged...
