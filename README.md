❤️ Heart Disease Prediction
📌 Project Overview

This project predicts the likelihood of heart disease based on patient health records using various Machine Learning models.
It demonstrates data preprocessing, model training, evaluation, and deployment with a Streamlit web application.

🎯 Objectives

Understand key health factors contributing to heart disease.

Train ML models to classify patients into disease / no-disease groups.

Build an interactive app for real-time predictions.

🛠 Workflow

1️⃣ Data Collection & Preprocessing

Load heart disease dataset

Clean, scale, and encode features

2️⃣ Model Training

Algorithms used: Logistic Regression, Random Forest, XGBoost, SVM, KNN

Evaluate using Accuracy, Precision, Recall, F1-Score

3️⃣ Model Selection & Saving

Choose best-performing model

Save using pickle / joblib

4️⃣ Streamlit App

Collect user inputs (age, sex, chest pain type, blood pressure, cholesterol, etc.)

Predict heart disease instantly

Show model insights

📊 Dataset Features

age → Patient age (years)

sex → Gender (0 = Female, 1 = Male)

cp → Chest pain type (0–3)

trestbps → Resting blood pressure (mm Hg)

chol → Serum cholesterol (mg/dL)

fbs → Fasting blood sugar >120 mg/dL (0 = No, 1 = Yes)

restecg → Resting ECG results (0–2)

thalach → Maximum heart rate achieved

exang → Exercise-induced angina (0 = No, 1 = Yes)

oldpeak → ST depression induced by exercise

slope → Slope of ST segment (0–2)

ca → Major vessels (0–3)

thal → Thalassemia result (1–3)

target → Heart disease presence (0 = No, 1 = Yes)

📦 Requirements

Python 3.10+

Libraries:

pandas

numpy

scikit-learn

xgboost

streamlit

pickle-mixin / joblib



📌 Results

Multiple ML models compared

Best accuracy achieved with XGBoost / RandomForest

Interactive predictions via Streamlit

🙌 Acknowledgments

Dataset inspired by the UCI Heart Disease Dataset.

Ttry it Here:- https://ml-project-heart-disease-predictor.streamlit.app/
