from sklearn.cluster import KMeans  
from sklearn.metrics import accuracy_score  
from sklearn.model_selection import train_test_split  
from sklearn.datasets import load_iris  
import numpy as np  

# Load the Iris dataset  
iris = load_iris()  
X, y = iris.data, iris.target  

# Split data into train and test sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Initialize and train the K-Means model  
kmeans = KMeans(n_clusters=3, random_state=42)  
kmeans.fit(X_train)  

# Predict on test data  
y_pred = kmeans.predict(X_test)  

# Align cluster labels with true labels (K-Means doesn't use labels)  
from sklearn.metrics import confusion_matrix  
conf_matrix = confusion_matrix(y_test, y_pred)  
# Find the best mapping between clusters and true labels  
from scipy.optimize import linear_sum_assignment  
row_ind, col_ind = linear_sum_assignment(-conf_matrix)  
y_pred_aligned = np.zeros_like(y_pred)  
for cluster, true_label in zip(row_ind, col_ind):  
    y_pred_aligned[y_pred == cluster] = true_label  

# Calculate and print accuracy  
accuracy = accuracy_score(y_test, y_pred_aligned)  
print(f'Accuracy (K-Means): {accuracy:.4f}')
