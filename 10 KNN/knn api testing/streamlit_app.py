import streamlit as st
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Page config
st.set_page_config(page_title="Churn Predictor", page_icon="🔮", layout="centered")

# Load model
@st.cache_resource
def load_model():
    return joblib.load('knn_model.pkl')

model = load_model()

# Title
st.title("🔮 Customer Churn Predictor")
st.markdown("Uses a **KNN model** trained on bank customer data to predict whether a customer will churn.")
st.divider()

# Input form
st.subheader("Customer Details")

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=5)

with col2:
    balance = st.number_input("Account Balance", min_value=0.0, value=50000.0, step=1000.0)
    num_of_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
    is_active_member = st.selectbox("Active Member?", ["Yes", "No"])
    estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0, step=1000.0)

st.divider()

# Predict button
if st.button("Predict Churn", use_container_width=True, type="primary"):

    # Encode inputs
    le = LabelEncoder()

    geo_map = {"France": 0, "Germany": 1, "Spain": 2}
    gender_map = {"Male": 1, "Female": 0}

    input_data = np.array([[
        credit_score,
        geo_map[geography],
        gender_map[gender],
        age,
        tenure,
        balance,
        num_of_products,
        1 if has_cr_card == "Yes" else 0,
        1 if is_active_member == "Yes" else 0,
        estimated_salary
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.subheader("Result")

    if prediction == 1:
        st.error("⚠️ This customer is **likely to churn**.")
    else:
        st.success("✅ This customer is **likely to stay**.")

    col_a, col_b = st.columns(2)
    col_a.metric("Probability of Staying", f"{probability[0]*100:.1f}%")
    col_b.metric("Probability of Churning", f"{probability[1]*100:.1f}%")