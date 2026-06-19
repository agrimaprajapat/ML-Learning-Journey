# Iris Flower Classification using K-Nearest Neighbors (KNN)

This project implements a K-Nearest Neighbors (KNN) classifier on the Iris dataset using Scikit-learn.

## Dataset
- Built-in Iris dataset from Scikit-learn
- 150 samples
- 4 input features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- 3 flower species:
  - Setosa
  - Versicolor
  - Virginica

## Algorithm
- K-Nearest Neighbors (KNN)
- Number of Neighbors (K): 3

## Libraries Used
- NumPy
- Pandas
- Scikit-learn

## Results
- Model Accuracy: **100% (1.0)**

## Steps Performed
1. Loaded the Iris dataset.
2. Split the dataset into training and testing sets.
3. Trained a KNN classifier with `n_neighbors=3`.
4. Predicted the target values for the test set.
5. Evaluated the model using accuracy score.

## Conclusion
The KNN model successfully classified Iris flower species and achieved perfect accuracy on the test dataset.