import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to train and evaluate a model
def train_and_evaluate(model, x_train, y_train, x_test, y_test):
    model.fit(x_train, y_train)  # Train the model
    y_pred = model.predict(x_test)  # Predict on test set
    accuracy = accuracy_score(y_test, y_pred)  # Calculate accuracy
    return accuracy

# Load the CSV file
df = pd.read_csv('../AttributeSelectionData.csv')

# Define features and target
X = df.drop(columns='Diagnosis')
y = df['Diagnosis']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the models
models = {
    'Naive Bayes': GaussianNB(),
    'Random Forest': RandomForestClassifier()
}

# Store the results
results = {}

# Train and evaluate each model
for model_name, model in models.items():
    accuracy = train_and_evaluate(model, X_train, y_train, X_test, y_test)
    results[model_name] = accuracy

# Print accuracies
for model_name, accuracy in results.items():
    print(f'{model_name} Accuracy: {accuracy:.2f}')

# Create a DataFrame for accuracies to plot
accuracy_data = pd.DataFrame(list(results.items()), columns=['Model', 'Accuracy'])

# Plot a bar chart to visualize the difference in accuracies
plt.figure(figsize=(10, 6))
plt.bar(accuracy_data['Model'], accuracy_data['Accuracy'], color=['blue', 'green'])
plt.title('Comparison of Model Accuracies')
plt.ylabel('Accuracy')
plt.show()
