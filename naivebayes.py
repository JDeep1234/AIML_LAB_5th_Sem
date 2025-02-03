import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
classes, mean, var, priors = np.unique(y), np.array([X_train[y_train == c].mean(0) for c in np.unique(y)]), np.array([X_train[y_train == c].var(0) for c in np.unique(y)]), np.array([(y_train == c).mean() for c in np.unique(y)])

predict = lambda x: classes[np.argmax([np.log(prior) + np.sum(np.log(np.exp(-(x - mean[i])**2 / (2 * var[i])) / np.sqrt(2 * np.pi * var[i]))) for i, prior in enumerate(priors)])]
y_pred = np.array([predict(x) for x in X_test])

print('Accuracy: %.4f' % np.mean(y_pred == y_test))
print("Predictions:", load_iris().target_names[y_pred])
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=load_iris().target_names))
