import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_iris

X, k = load_iris().data, 3
centroids = X[np.random.choice(X.shape[0], k, replace=False)]

for _ in range(100):
    labels = np.argmin(np.linalg.norm(X[:, None] - centroids, axis=2), axis=1)
    centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

for i, c in enumerate(['r', 'g', 'b']):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], c=c, label=f'Cluster {i+1}')
    
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='black', label='Centroids')
plt.title('K-Means Clustering on Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(), plt.show()
