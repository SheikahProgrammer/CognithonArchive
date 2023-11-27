import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix  # Import the function

# Load the dataset
df = pd.read_csv("pleaseee.csv", header=0)
df = df.round(3)

# Define the target variable (y) and features (X)
y = df[['o1', 'o2', 'o3', 'o4', 'o5', 'o6']]
X = df[['pressure', 'temp', 'vibe', 'flow', 'level', 'rpm']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Initialize the DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)

# Define a parameter grid to search through
param_grid = {
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Perform grid search with cross-validation
grid_search = GridSearchCV(estimator=clf, param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_

# Initialize a new classifier with the best parameters
clf = DecisionTreeClassifier(random_state=42, **best_params)

# Fit the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Print classification report and confusion matrix
# Evaluate the model's performance

# Your single input data as a 1D array
input_data = np.array([38.1483, 48, 4.651165, 12.3786, 70.2287, 916.365])

# Reshape the input data to a 2D array with a single sample
input_data_2d = input_data.reshape(1, -1)

# Predict using the reshaped input data
predicted_value = clf.predict(input_data_2d)
print(predicted_value)

import joblib

# Save the model to a file
joblib.dump(clf, 'decision_tree_model.joblib')

# To load the model later, you can use:
# clf = joblib.load('decision_tree_model.joblib')

# Compute the multi-label confusion matrix
multi_label_confusion = multilabel_confusion_matrix(y_test, y_pred)

# Display the multi-label confusion matrix for each class
for i, label in enumerate(['o1', 'o2', 'o3', 'o4', 'o5', 'o6']):
    print(f"Confusion Matrix for {label}:")
    print(multi_label_confusion[i])
    print()

# Calculate label-based accuracy for each class
label_based_accuracies = []
for i, label in enumerate(['o1', 'o2', 'o3', 'o4', 'o5', 'o6']):
    tn, fp, fn, tp = multi_label_confusion[i].ravel()
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    label_based_accuracies.append(accuracy)
    print(f"Accuracy for {label}: {accuracy:.3f}")

# Calculate and print the average label-based accuracy
average_label_accuracy = sum(label_based_accuracies) / len(label_based_accuracies)
print(f"Average Label-Based Accuracy: {average_label_accuracy:.3f}")

