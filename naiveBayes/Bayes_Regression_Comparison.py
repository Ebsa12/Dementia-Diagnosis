""" 
Author: Zak Groenewold
Date: 11/14/2024
Logistic Regression and Naive Bayes comparison
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


#Load dataset
data = "BalancedData.csv"
df = pd.read_csv(data)

x = df.drop(columns = 'Diagnosis')
y = df['Diagnosis']

#Split data into test and training sets
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=42)

#Initialize Logistic Regression model
logistic_regression = LogisticRegression(max_iter=1000)

#Train Logistic Regression model
logistic_regression.fit(x_train, y_train)

#Predict with test set
log_regress_prediction = logistic_regression.predict(x_test)

#Find accuracy, precision, recall, and F1 score of Logistic Regression model
logistic_regression_accuracy = accuracy_score(y_test, log_regress_prediction)
lg_precision = precision_score(y_test, log_regress_prediction, pos_label='Yes')
lg_recall = recall_score(y_test, log_regress_prediction, pos_label='Yes')
lg_fscore = f1_score(y_test, log_regress_prediction, pos_label='Yes')

# Find average score for Logistic Regression model
lg_average = (logistic_regression_accuracy + lg_precision + lg_recall + lg_fscore) / 4

#Initialize Naive Bayes model
naive_bayes = GaussianNB()

#Train Naive Bayes model
naive_bayes.fit(x_train, y_train)

#Make predictions with test set
naive_bayes_prediction = naive_bayes.predict(x_test)

#Find accuracy, precision, recall, and F1 score for Naive Bayes Model
bayes_accuracy = accuracy_score(y_test, naive_bayes_prediction)
nb_precision = precision_score(y_test, naive_bayes_prediction, pos_label='Yes')
nb_recall = recall_score(y_test, naive_bayes_prediction, pos_label='Yes')
nb_fscore = f1_score(y_test, naive_bayes_prediction, pos_label='Yes')

#Find average for Naive Bayes model
nb_average = (bayes_accuracy + nb_precision + nb_recall + nb_fscore) / 4

#Print accuracy of each algorithm
print(f'Logistic Regression Accuracy: {logistic_regression_accuracy:.2f}')
print(f'Logistic Regression Recall: {lg_recall:.2f}')
print(f'Logistic Regression Precision: {lg_precision:.2f}')
print(f'Logistic Regression F1 Score: {lg_fscore:.2f}')
print('')

print(f'Naive Bayes Accuracy: {bayes_accuracy:.2f}')
print(f'Naive Bayes Recall: {nb_recall:.2f}')
print(f'Naive Bayes Precision: {nb_precision:.2f}')
print(f'Naive Bayes F1 Score: {nb_fscore:.2f}')
print('')
print('The average score of each algorithm is shown below:')
print(f'Naive Bayes: {nb_average:.3f}    Logistic Regression: {lg_average:.3f}')

# Create a DataFrame for accuracies to plot
accuracy_data = pd.DataFrame({
    'Model': ['Logistic Regression', 'Naive Bayes'],
    'Accuracy': [logistic_regression_accuracy, bayes_accuracy]
})
# Bar plot algorithm comparison
fig = plt.figure(figsize=(10,6))
plt.ylim(0,1.0)
fig.suptitle('Algorithm Comparison')
plt.bar(accuracy_data['Model'], accuracy_data['Accuracy'], color=['red','green'])
plt.ylabel('Accuracy')
plt.show()
