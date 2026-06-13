# COVID Prediction using Logistic Regression

A machine learning project that predicts whether a person has COVID-19 based on symptoms and demographic information. The model is trained using Logistic Regression and saved using Joblib for future use.

## Features

* Age
* Gender
* Fever
* Cough
* City

**Target:** Has_Covid

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Preprocessing

Categorical features were converted into numerical values using Label Encoding:

* Gender
* Cough
* City
* Has_Covid

## Model Training

* Train-test split using `train_test_split()`
* Logistic Regression classifier
* Performance evaluated using Accuracy Score

**Accuracy:** ~75%

```

## Project Structure

```text
covid-prediction/
├── LogisticRegression.ipynb
├── LogisticRegression.pkl
├── readme.md
└── covid_toy.csv
```

## Learning Outcomes

* Data preprocessing and Label Encoding
* Logistic Regression for classification
* Model evaluation using accuracy
* Saving and loading models with Joblib
* Building an end-to-end machine learning workflow
