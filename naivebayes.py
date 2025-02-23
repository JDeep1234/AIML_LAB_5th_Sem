import numpy as np  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split  

# Load iris dataset  
iris = load_iris()  
X, y = iris.data, iris.target  

class NaiveBayes:  
    def fit(self, X, y):  
        self.classes = np.unique(y)  
        self.means = np.array([X[y == c].mean(axis=0) for c in self.classes])  
        self.vars = np.array([X[y == c].var(axis=0) for c in self.classes])  
        self.priors = np.array([X[y == c].shape[0] / len(y) for c in self.classes])  

    def predict(self, X):  
        return np.array([self._predict(x) for x in X])  

    def _predict(self, x):  
        posteriors = [np.log(prior) + np.sum(np.log(self._pdf(idx, x)))  
                      for idx, prior in enumerate(self.priors)]  
        return self.classes[np.argmax(posteriors)]  

    def _pdf(self, class_idx, x):  
        mean, var = self.means[class_idx], self.vars[class_idx]  
        return np.exp(-(x - mean)**2 / (2 * var)) / np.sqrt(2 * np.pi * var)  

# Split the dataset  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  

# Train and predict  
nb = NaiveBayes()  
nb.fit(X_train, y_train)  
y_pred = nb.predict(X_test)  

# Results  
print('Accuracy: %.4f' % np.mean(y_pred == y_test))  
print("Predictions:", iris.target_names[y_pred])  

# Optional confusion matrix and classification report  
from sklearn.metrics import confusion_matrix, classification_report  
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))  
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))
