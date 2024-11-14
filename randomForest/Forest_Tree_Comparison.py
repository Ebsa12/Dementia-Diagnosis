""" 
Author: Zak Groenewold
Date: 11/14/2024
Decision Tree and Random Forest comparison
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

#Load dataset
data = "BalancedData.csv"
df = pd.read_csv(data)

x = df.drop(columns = 'Diagnosis')
y = df['Diagnosis']

#Split data into test and training sets
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=42)

#Initialize Decision Tree
decision_tree = DecisionTreeClassifier()

#Train Logistic Regression model
decision_tree.fit(x_train, y_train)

#Predict with test set
decision_tree_prediction = decision_tree.predict(x_test)

#Find decision tree precision, recall, accuracy and f1 score
decision_tree_accuracy = accuracy_score(y_test, decision_tree_prediction)
dt_recall = recall_score(y_test, decision_tree_prediction, pos_label='Yes')
dt_precision = precision_score(y_test, decision_tree_prediction, pos_label='Yes')
dt_fscore  = f1_score(y_test, decision_tree_prediction, pos_label='Yes')

#Find average score 
dt_average_score = (decision_tree_accuracy + dt_recall + dt_precision + dt_fscore) / 4

#Initialize Random Forest model
random_forest = RandomForestClassifier()

#Train Random Forest model
random_forest.fit(x_train, y_train)

#Make predictions with test set
rf_prediction = random_forest.predict(x_test)

#Find accuracy, recall, precision, and f1 score for Random Forest Model
rf_accuracy = accuracy_score(y_test, rf_prediction)
rf_recall = recall_score(y_test, rf_prediction, pos_label='Yes')
rf_precision = precision_score(y_test, rf_prediction, pos_label='Yes') 
rf_fscore= f1_score(y_test, rf_prediction, pos_label="Yes")

#Find average score
rf_average_score = (rf_accuracy + rf_recall + rf_precision + rf_fscore) / 4

#Print accuracy of each algorithm
print(f'Decision Tree Accuracy: {decision_tree_accuracy:.2f}')
print(f'Decision Tree Recall: {dt_recall:.2f}')
print(f'Decision Tree Precision: {dt_precision:.2f}')
print(f'Decision Tree F1 Score: {dt_fscore:.2f}')
print('')
print(f'Random Forest Accuracy: {rf_accuracy:.2f}')
print(f'Random Forest Recall: {rf_recall:.2f}')
print(f'Random Forest Precision: {rf_precision:.2f}')
print(f'Random Forest F1 Score: {rf_fscore:.2f}')
print('')
print('The average score of each algorithm is shown below:')
print(f'Decicion Tree: {dt_average_score:.3f}   Random Forest: {rf_average_score:.3f}')

# Create a DataFrame for accuracies to plot
accuracy_data = pd.DataFrame({
    'Model': ['Random Forest', 'Decision Tree'],
    'Accuracy': [rf_accuracy, decision_tree_accuracy]
})
# Bar plot algorithm comparison
fig = plt.figure(figsize=(10,6))
plt.ylim(0, 1.0)
fig.suptitle('Algorithm Comparison')
plt.bar(accuracy_data['Model'], accuracy_data['Accuracy'], color=['red','green'])
plt.ylabel('Accuracy')
plt.show()
