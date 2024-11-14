import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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

# Calculate Precision with Logistic Regression
precision_log_reg = precision_score(y_test, y_pred_log_reg, pos_label='Yes')

#Calculate Recall with Logistic Regression
recall_log_reg = recall_score(y_test, y_pred_log_reg, pos_label='Yes')

# Calculate f1 with Logistic Regression
f1_log_reg = f1_score(y_test, y_pred_log_reg, pos_label='Yes')

# Initialize the Random Forest model
rf = RandomForestClassifier()

# Train the Random Forest model
rf.fit(X_train, y_train)

# Make predictions with Random Forest
y_pred_rf = rf.predict(X_test)

# Calculate accuracy for Random Forest
accuracy_rf = accuracy_score(y_test, y_pred_rf)

# Calculate Precision with Random Forest
precision_rf = precision_score(y_test, y_pred_rf, pos_label='Yes')

#Calculate Recall with Random Forest
recall_rf = recall_score(y_test, y_pred_rf, pos_label='Yes')

# Calculate f1 with Random Forest
f1_rf = f1_score(y_test, y_pred_rf, pos_label='Yes')

# Calculate Average recall, accuracy and precision for Logistic Regression
average_log_reg = (accuracy_log_reg + precision_log_reg + recall_log_reg + f1_log_reg) / 4

# Calculate Average recall, accuracy and precision for Random Forest
average_rf = (accuracy_rf + precision_rf + recall_rf + f1_rf) / 4

print(f'average Log Reg: {average_log_reg:.3f}')
print(f'average random forest: {average_rf:.3f}')

# # Print accuracies
# print(f'Logistic Regression Accuracy: {accuracy_log_reg:.2f}')
# print(f'Random Forest Accuracy: {accuracy_rf:.2f}')

# # Print precisions
# print(f'Logistic Regression Precision: {precision_log_reg:.2f}')
# print(f'Random Forest Precision: {precision_rf:.2f}')

# # Print recalls
# print(f'Logistic Regression Recall: {recall_log_reg:.2f}')
# print(f'Random Forest Recall: {recall_rf:.2f}')

# Create a DataFrame for accuracies to plot
average_data = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest'],
    'Averages': [average_log_reg, average_rf]
})


# Plot a bar chart to visualize the difference in accuracies
# Plot a bar chart to visualize the difference in recall
plt.figure(figsize=(10, 6))
plt.bar(average_data['Model'], average_data['Averages'], color=['blue', 'green'])
plt.title('Comparison of Model Machine Learning Averages')
plt.ylabel('Averages')
plt.show()
