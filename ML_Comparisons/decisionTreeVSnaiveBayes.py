import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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
# Calculate f1 for Naive Bayes
f1_nb = f1_score(y_test, y_pred_nb, pos_label='Yes')

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
# Calculate f1 for Decision Tree
f1_dt = f1_score(y_test, y_pred_dt, pos_label='Yes')

# Calculate Averages
Average_dt = (accuracy_dt + precision_dt + recall_dt + f1_dt) / 4
Average_nb = (accuracy_nb + precision_nb + recall_nb + f1_nb) / 4

# Print averages
print(f"Average Decision Tree: {Average_dt:.3f}")
print(f"Average Naive Bayes: {Average_nb:.3f}")

# Create a DataFrame for accuracies to plot
average_data = pd.DataFrame({
    'Model': ['Naive Bayes', 'Decision Tree'],
    'Average': [Average_nb, Average_dt]
})

# Plot a bar chart to visualize the difference in accuracies
plt.figure(figsize=(10, 6))
plt.bar(average_data['Model'], average_data['Average'], color=['blue', 'green'])
plt.title('Comparison of Model Averages')
plt.ylabel('Average')
plt.show()