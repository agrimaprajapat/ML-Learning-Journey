# 🔮 churn-predictor-knn


This project trains a KNN model on the [Churn Modelling dataset] to predict whether a bank customer is likely to leave. The trained model is saved with `joblib` and exposed through two interfaces:

- **Streamlit app** — interactive browser UI for manual predictions
- **Flask API** — lightweight REST endpoint for programmatic access

---

## Application Preview

![Customer Churn Predictor](images/churn_knn.png.png)

## Project Structure

```
churn-predictor-knn/
├── app.py                  # Flask REST API
├── streamlit_app.py        # Streamlit frontend
├── model_training.py       # Model training script
├── knn_model.pkl           # Saved KNN model (generated after training)
├── Churn_Modelling.csv     # Dataset (download separately)
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/churn-predictor-knn.git
cd churn-predictor-knn
```

### 2. Install dependencies

Using `uv` (recommended):
```bash
uv sync
```

Or with pip:
```bash
pip install -r requirements.txt
```

### 3. Add the dataset

Download `Churn_Modelling.csv` from [Kaggle](https://www.kaggle.com/datasets/shubh0799/churn-modelling) and place it in the project root.

### 4. Train the model

```bash
python model_training.py
```

This will train a KNN classifier (k=7), print the accuracy, and save `knn_model.pkl`.

---

## Running the App

### Streamlit UI

```bash
streamlit run streamlit_app.py
```

Open your browser at `http://localhost:8501`. Fill in the customer details form and click **Predict Churn**.

### Flask API

```bash
python app.py
```

The API runs at `http://localhost:5000`. Send a POST request to `/predict`:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": [600, 0, 1, 35, 5, 50000, 2, 1, 1, 60000]}'
```

**Input feature order:**
`CreditScore, Geography (encoded), Gender (encoded), Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary`

**Response:**
```json
{ "prediction": 0 }
```
`0` = likely to stay, `1` = likely to churn.

---

## Model Details

| Parameter | Value |
|-----------|-------|
| Algorithm | K-Nearest Neighbors |
| k (neighbors) | 7 |
| Train/Test Split | 80% / 20% |
| Random State | 42 |
| Encoding | LabelEncoder (Geography, Gender) |

---

## Features Used

| Feature | Description |
|---------|-------------|
| CreditScore | Customer credit score |
| Geography | Country (France / Germany / Spain) |
| Gender | Male / Female |
| Age | Customer age |
| Tenure | Years with the bank |
| Balance | Account balance |
| NumOfProducts | Number of bank products held |
| HasCrCard | Whether the customer has a credit card |
| IsActiveMember | Whether the customer is an active member |
| EstimatedSalary | Estimated annual salary |

---

## License

MIT