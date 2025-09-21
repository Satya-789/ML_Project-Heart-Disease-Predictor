import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model and scaler
with open("heart_disease.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details to predict the risk of heart disease.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", (0, 1), format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", (0, 1, 2, 3),
                  format_func=lambda x: ["Typical Angina","Atypical Angina","Non-anginal Pain","Asymptomatic"][x])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", (0, 1), format_func=lambda x: "No" if x == 0 else "Yes")
restecg = st.selectbox("Resting ECG Results", (0, 1, 2),
                       format_func=lambda x: ["Normal","ST-T Abnormality","Left Ventricular Hypertrophy"][x])
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina", (0, 1), format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment", (0, 1, 2), format_func=lambda x: ["Upsloping","Flat","Downsloping"][x])
ca = st.selectbox("Number of Major Vessels (0–3)", (0, 1, 2, 3))
thal_options = {1: "Fixed Defect", 2: "Normal", 3: "Reversible Defect"}
thal = st.selectbox("Thalassemia", options=list(thal_options.keys()),
                    format_func=lambda x: thal_options[x])


# Collect inputs into array
# Collect inputs into array
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

# Convert to DataFrame with column names
columns = ["age","sex","cp","trestbps","chol","fbs","restecg",
           "thalach","exang","oldpeak","slope","ca","thal"]
input_df = pd.DataFrame(input_data, columns=columns)

# Scale input
input_data_scaled = scaler.transform(input_df)


# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data_scaled)
    if prediction[0] == 1:
        st.error("⚠️ The patient is likely to have heart disease.")
    else:
        st.success("✅ The patient is unlikely to have heart disease.")
