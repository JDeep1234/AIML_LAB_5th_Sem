import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Load dataset
X, y = load_iris(return_X_y=True)
class_names = load_iris().target_names

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Compute class-wise mean, variance, and prior probabilities
classes = np.unique(y)
mean = np.array([X_train[y_train == c].mean(axis=0) for c in classes])
var = np.array([X_train[y_train == c].var(axis=0) for c in classes])
priors = np.array([(y_train == c).mean() for c in classes])

# Naïve Bayes prediction function
def predict(x):
    probs = [
        np.log(priors[i]) + np.sum(
            np.log(np.exp(-(x - mean[i])**2 / (2 * var[i])) / np.sqrt(2 * np.pi * var[i]))
        )
        for i in range(len(classes))
    ]
    return classes[np.argmax(probs)]

# Predict on test set
y_pred = np.array([predict(x) for x in X_test])

# Print results
accuracy = np.mean(y_pred == y_test)
print(f'Accuracy: {accuracy:.4f}')
print("Predictions:", class_names[y_pred])
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=class_names))
