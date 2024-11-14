from decisionTreeVSnaiveBayes import Average_dt, Average_nb
from logisticRegressionVSRandomForest import average_log_reg, average_rf
import matplotlib.pyplot as plt
import pandas as pd

print(f"Average Decision Tree: {Average_dt:.3f}")
print(f'average random forest: {average_rf:.3f}')
print(f"Average Naive Bayes: {Average_nb:.3f}")
print(f'average Log Reg: {average_log_reg:.3f}')

average_data = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest', 'Naive Bayes', 'Decision Tree'],
    'Averages': [average_log_reg, average_rf, Average_nb, Average_dt]
})


plt.figure(figsize=(10, 6))
plt.bar(average_data['Model'], average_data['Averages'], color=['red', 'blue', 'orange', 'purple'])
plt.title('Comparison of Machine Learning Algorithms')
plt.ylabel('Averages')
plt.show()
