from sklearn.naive_bayes import GaussianNB  
from sklearn.metrics import accuracy_score  
from sklearn.model_selection import train_test_split  
from sklearn.datasets import load_iris  

# Load the Iris dataset  
iris = load_iris()  
X, y = iris.data, iris.target  

# Split data into train and test sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Initialize and train the Naive Bayes model  
nb = GaussianNB()  
nb.fit(X_train, y_train)  

# Predict on test data  
y_pred = nb.predict(X_test)  

# Calculate and print accuracy  
accuracy = accuracy_score(y_test, y_pred)  
print(f'Accuracy (Naive Bayes): {accuracy:.4f}')
