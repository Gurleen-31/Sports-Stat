import streamlit as st
from overview import show_overview
from exploration import show_exploration
from model_training import show_model_training
from prediction import show_prediction
import pandas as pd

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("sports_data.csv")
        st.success("✅ Data loaded")
        return df
    except Exception as e:
        st.error(f"❌ Could not load CSV: {e}")
        return pd.DataFrame()
@st.cache_resource
def load_model():
    try:
        model = joblib.load("sports_model.pkl")
        st.success("✅ Model loaded")
        return model
    except Exception as e:
        st.error(f"❌ Could not load model: {e}")
        return None

# Configure page
st.set_page_config(page_title="BasketballStatsExplorer", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Overview",
    "Data Exploration",
    "Model Training",
    "Prediction"
])

# Load data
df = load_data()

# Display the selected page
if page == "Overview":
    show_overview(df)
elif page == "Data Exploration":
    show_exploration(df)
elif page == "Model Training":
    show_model_training(df)
elif page == "Prediction":
    show_prediction(df)
