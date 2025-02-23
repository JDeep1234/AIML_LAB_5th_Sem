import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter

X, y, names = *load_iris(return_X_y=True), load_iris().target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
predict = lambda X: np.array([Counter(y_train[np.argsort([np.linalg.norm(x - x_train) for x_train in X_train])[:3]]).most_common(1)[0][0] for x in X])
y_pred = predict(X_test)

print(f'Accuracy: {np.mean(y_pred == y_test):.4f}', "\nPredictions:", names[y_pred], "\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred), "\nClassification Report:\n", classification_report(y_test, y_pred, target_names=names))
print(f'Accuracy: {np.mean(y_pred == y_test):.4f}',
      "\nPredictions:", names[y_pred], "\nConfusion Matrix:\n", 
      confusion_matrix(y_test, y_pred), 
      "\nClassification Report:\n", 
      classification_report(y_test, y_pred, target_names=names))
