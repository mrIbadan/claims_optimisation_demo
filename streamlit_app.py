import streamlit as st
import joblib

# Load the model
model = joblib.load("best_claims_model.pkl")

st.title("Home Insurance Claims Prediction")

# Input form
st.header("Enter Claim Details")
incident_type = st.selectbox("Incident Type", ["Escape of Water", "Fire", "Theft"])
property_type = st.selectbox("Property Type", ["House", "Flat", "Bungalow"])
property_value = st.number_input("Property Value (£)", min_value=50000, max_value=2000000, step=10000)
resolution_time = st.number_input("Resolution Time (days)", min_value=1, max_value=100)
region = st.selectbox("Region", ["North West", "South East", "London"])
claim_month = st.slider("Month of Claim", 1, 12)
claim_year = st.slider("Year of Claim", 2019, 2024)

# Predict
if st.button("Predict Claim Amount"):
    input_data = pd.DataFrame({
        "Incident_Type": [incident_type],
        "Property_Type": [property_type],
        "Property_Value (£)": [property_value],
        "Resolution_Time (days)": [resolution_time],
        "Region": [region],
        "Claim_Year": [claim_year],
        "Claim_Month": [claim_month],
    })
    predicted_claim = model.predict(input_data)[0]
    st.success(f"Predicted Claim Amount: £{predicted_claim:,.2f}")
