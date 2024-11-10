import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the CSV file into a DataFrame
df = pd.read_csv('../AttributeSelectionData.csv')

# Define features and target
X = df.drop(columns='Diagnosis')
y = df['Diagnosis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
log_reg = LogisticRegression(max_iter=1000)

# Train the Logistic Regression model
log_reg.fit(X_train, y_train)

# Make predictions with Logistic Regression
y_pred_log_reg = log_reg.predict(X_test)

# Calculate accuracy for Logistic Regression
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)

# Initialize the Random Forest model
rf = RandomForestClassifier()

# Train the Random Forest model
rf.fit(X_train, y_train)

# Make predictions with Random Forest
y_pred_rf = rf.predict(X_test)

# Calculate accuracy for Random Forest
accuracy_rf = accuracy_score(y_test, y_pred_rf)

# Print accuracies
print(f'Logistic Regression Accuracy: {accuracy_log_reg:.2f}')
print(f'Random Forest Accuracy: {accuracy_rf:.2f}')

# Create a DataFrame for accuracies to plot
accuracy_data = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest'],
    'Accuracy': [accuracy_log_reg, accuracy_rf]
})

# Plot a bar chart to visualize the difference in accuracies
plt.figure(figsize=(10, 6))
plt.bar(accuracy_data['Model'], accuracy_data['Accuracy'], color=['blue', 'green'])
plt.title('Comparison of Model Accuracies')
plt.ylabel('Accuracy')
plt.show()
