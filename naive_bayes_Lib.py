from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = np.array(iris.target_names)  # Get class names

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Multinomial Naïve Bayes model
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Predict on test data
y_pred = nb.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Print predictions with class names
print("Predictions:", class_names[y_pred])

# Print confusion matrix
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Print classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=class_names))
