import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the CSV file
df = pd.read_csv('../AttributeSelectionData.csv')

# Define features and target
x = df.drop(columns='Diagnosis')
y = df['Diagnosis']

# Split the data into training and test sets
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=42)

# Logistic Regression model
log_reg = LogisticRegression(max_iter=1000)

# Train the Logistic Regression model
log_reg.fit(x_train, y_train)

# Make predictions with Logistic Regression
y_pred_log_reg = log_reg.predict(x_test)

# Calculate accuracy for the Logistic Regression model
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)

# Initialize the Decision Tree model
dt = DecisionTreeClassifier()

# Train the Decision Tree model
dt.fit(x_train, y_train)

# Make predictions with Decision Tree
y_pred_dt = dt.predict(x_test)

# Calculate accuracy for the Decision Tree model
accuracy_dt = accuracy_score(y_test, y_pred_dt)

# Print accuracies
print(f'Logistic Regression Accuracy: {accuracy_log_reg:.2f}')
print(f'Decision Tree Accuracy: {accuracy_dt:.2f}')

# Create a DataFrame for accuracies to plot
accuracy_data = pd.DataFrame({
    'Model': ['Logistic Regression', 'Decision Tree'],
    'Accuracy': [accuracy_log_reg, accuracy_dt]
})

# Plot a bar chart to visualize the difference in accuracies
plt.figure(figsize=(10, 6))
plt.bar(accuracy_data['Model'], accuracy_data['Accuracy'], color=['brown', 'red'])
plt.title('Comparison of Model Accuracies')
plt.ylabel('Accuracy')
plt.show()
