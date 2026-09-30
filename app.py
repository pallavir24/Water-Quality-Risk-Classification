import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Water Quality Risk Classifier", layout="centered")

st.title("💧 Water Quality Risk Classification Prototype")
st.write("Enter physical and chemical characteristics to evaluate potability risk.")

@st.cache_resource
def load_model():
    with open("water_model.pkl", "rb") as f:
        payload = pickle.load(f)
    return payload["model"]

model = load_model()

st.subheader("Water Parameters")
col1, col2 = st.columns(2)

with col1:
    ph = st.slider("pH Level", 0.0, 14.0, 7.0, step=0.1)
    hardness = st.slider("Hardness (mg/L)", 50.0, 350.0, 196.0, step=1.0)
    solids = st.slider("Solids / TDS (ppm)", 500.0, 50000.0, 22000.0, step=100.0)
    chloramines = st.slider("Chloramines (ppm)", 0.0, 15.0, 7.1, step=0.1)
    sulfate = st.slider("Sulfate (mg/L)", 100.0, 500.0, 333.0, step=1.0)

with col2:
    conductivity = st.slider("Conductivity (μS/cm)", 100.0, 800.0, 426.0, step=1.0)
    organic_carbon = st.slider("Organic Carbon (ppm)", 2.0, 30.0, 14.2, step=0.1)
    trihalomethanes = st.slider("Trihalomethanes (μg/L)", 0.0, 130.0, 66.3, step=0.1)
    turbidity = st.slider("Turbidity (NTU)", 1.0, 7.0, 3.9, step=0.1)

input_data = np.array([[ph, hardness, solids, chloramines, sulfate, 
                        conductivity, organic_carbon, trihalomethanes, turbidity]])

st.write("---")

if st.button("Predict Water Safety / Risk", use_container_width=True):
    prediction = model.predict(input_data)[0]
    
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_data)[0]
        safe_prob = proba[1] * 100
        risk_prob = proba[0] * 100
    else:
        safe_prob = 100 if prediction == 1 else 0
        risk_prob = 100 - safe_prob

    if prediction == 1:
        st.success(f"✅ Safe / Potable Water (Confidence: {safe_prob:.1f}%)")
    else:
        st.error(f"⚠️ High Risk / Non-Potable Water (Risk: {risk_prob:.1f}%)")