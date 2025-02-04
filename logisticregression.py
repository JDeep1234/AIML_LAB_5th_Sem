import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and preprocess data
data = load_iris()
X, y = data.data[:, :2], (data.target != 0).astype(int)  # Binary classification
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Train logistic regression (gradient descent)
w = np.zeros(X_train.shape[1])
lr, epochs = 0.1, 5000

for _ in range(epochs):
    w -= lr * X_train.T @ (sigmoid(X_train @ w) - y_train) / len(y_train)

# Plot decision boundary
xx, yy = np.meshgrid(np.arange(X_train[:, 0].min()-1, X_train[:, 0].max()+1, 0.1),
                     np.arange(X_train[:, 1].min()-1, X_train[:, 1].max()+1, 0.1))

zz = sigmoid(np.c_[xx.ravel(), yy.ravel()] @ w).reshape(xx.shape)
plt.contourf(xx, yy, zz > 0.5, alpha=0.4)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, alpha=0.8)
plt.title('Logistic Regression Decision Boundary')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.savefig('plot.png')

# Print accuracy
accuracy = np.mean((sigmoid(X_test @ w) > 0.5) == y_test)
print(f'Accuracy: {accuracy:.4f}')
