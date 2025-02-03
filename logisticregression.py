import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sigmoid = lambda z: 1 / (1 + np.exp(-z))
X, y = load_iris().data[:, :2], (load_iris().target != 0) * 1
X_train, X_test, y_train, y_test = train_test_split(StandardScaler().fit_transform(X), y, test_size=0.2, random_state=42)

w = np.zeros(X_train.shape[1])
for _ in range(5000): w -= 0.1 * np.dot(X_train.T, (sigmoid(X_train @ w) - y_train)) / y_train.size

xx, yy = np.meshgrid(np.arange(X_train[:, 0].min()-1, X_train[:, 0].max()+1, 0.1),
                     np.arange(X_train[:, 1].min()-1, X_train[:, 1].max()+1, 0.1))

plt.contourf(xx, yy, sigmoid(np.c_[xx.ravel(), yy.ravel()] @ w).reshape(xx.shape) > 0.5, alpha=0.4)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, alpha=0.8), plt.title('Logistic Regression Decision Boundaries')
plt.xlabel('Sepal length'), plt.ylabel('Sepal width'), plt.savefig('plot.png'), print(f'Accuracy: {np.mean((sigmoid(X_test @ w) > 0.5) == y_test):.4f}')
