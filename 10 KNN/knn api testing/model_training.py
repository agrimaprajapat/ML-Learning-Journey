#importing libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

#load dataset
data = pd.read_csv('Churn_Modelling.csv')

#preprocessing

X = data.drop(['RowNumber', 'CustomerId', 'Surname', 'Exited'], axis=1)
y = data['Exited']

#encode categorical variables
le = LabelEncoder()
X['Geography'] = le.fit_transform(X['Geography'])
X['Gender'] = le.fit_transform(X['Gender'])


#split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the model
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

#make predictions
y_pred = knn.predict(X_test)
#evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

import joblib
#save the model
joblib.dump(knn, 'knn_model.pkl')

