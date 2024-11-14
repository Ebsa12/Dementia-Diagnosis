import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the CSV file into a DataFrame
df = pd.read_csv('../AttributeSelectionData.csv')

# Define features and target
X = df.drop(columns='Diagnosis')
y = df['Diagnosis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes model
nb = GaussianNB()

# Train the Naive Bayes model
nb.fit(X_train, y_train)

# Make predictions with Naive Bayes
y_pred_nb = nb.predict(X_test)

# Calculate accuracy for Naive Bayes
accuracy_nb = accuracy_score(y_test, y_pred_nb)
# Calculate Precision for Naive Bayes
precision_nb = precision_score(y_test, y_pred_nb, pos_label='Yes')
# Calculate Recall for Naive Bayes
recall_nb = recall_score(y_test, y_pred_nb, pos_label='Yes')

# Initialize the Decision Tree model
dt = DecisionTreeClassifier()

# Train the Decision Tree model
dt.fit(X_train, y_train)

# Make predictions with Decision Tree
y_pred_dt = dt.predict(X_test)

# Calculate accuracy for Decision Tree
accuracy_dt = accuracy_score(y_test, y_pred_dt)
# Calculate Precision for Decision Tree
precision_dt = precision_score(y_test, y_pred_dt, pos_label='Yes')
# Calculate Recall for Decision Tree
recall_dt = recall_score(y_test, y_pred_dt, pos_label='Yes')

# Print accuracies
print(f'Naive Bayes Accuracy: {accuracy_nb:.2f}')
print(f'Decision Tree Accuracy: {accuracy_dt:.2f}')

# Print precisions
print(f'Naive Bayes Precision: {precision_nb:.2f}')
print(f'Decision Tree Precision: {precision_dt:.2f}')

# Print recalls
print(f'Naive Bayes Recall: {recall_nb:.2f}')
print(f'Decision Tree Recall: {recall_dt:.2f}')

# Create a DataFrame for accuracies to plot
accuracy_data = pd.DataFrame({
    'Model': ['Naive Bayes', 'Decision Tree'],
    'Accuracy': [accuracy_nb, accuracy_dt]
})

# Create a DataFrame for precisions to plot
precision_data = pd.DataFrame({
    'Model': ['Naive Bayes', 'Decision Tree'],
    'Precision': [precision_nb, precision_dt]
})

# Create a DataFrame for recalls to plot
recall_data = pd.DataFrame({
    'Model': ['Naive Bayes', 'Decision Tree'],
    'Recall': [recall_nb, recall_dt]
})

# Plot a bar chart to visualize the difference in accuracies
plt.figure(figsize=(10, 6))
plt.bar(accuracy_data['Model'], accuracy_data['Accuracy'], color=['blue', 'green'])
plt.title('Comparison of Model Accuracies')
plt.ylabel('Accuracy')

# Plot a bar chart to visualize the difference in precision
plt.figure(figsize=(10, 6))
plt.bar(precision_data['Model'], precision_data['Precision'], color=['blue', 'green'])
plt.title('Comparison of Model Precision Metrics')
plt.ylabel('Precision')

# Plot a bar chart to visualize the difference in recall
plt.figure(figsize=(10, 6))
plt.bar(recall_data['Model'], recall_data['Recall'], color=['blue', 'green'])
plt.title('Comparison of Model Recall Metric')
plt.ylabel('Recall')
plt.show()