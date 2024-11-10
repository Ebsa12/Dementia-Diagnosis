import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated data for boxplot (multiple accuracy values for each model)
data = {
    "Model": ["Decision Tree"] * 50 + ["Logistic Regression"] * 50,
    "Accuracy": np.concatenate([
        np.random.normal(0.989, 0.01, 50),  # Simulating some variance around 0.989 for Decision Tree
        np.random.normal(0.831, 0.01, 50)   # Simulating some variance around 0.831 for Logistic Regression
    ])
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting the box-and-whisker plot
plt.figure(figsize=(8, 5))
sns.boxplot(x="Model", y="Accuracy", data=df, palette="Set2", showfliers=True)  # showfliers=True includes outliers as dots
plt.title("Algorithm Comparison")
plt.ylim(0, 1)  # Set y-axis to range from 0 to 1 for accuracy

# Displaying the plot
plt.show()

# Now, let's calculate the exact numbers (median, quartiles, and whiskers)
summary_stats = df.groupby("Model")["Accuracy"].describe()
print("Summary Statistics for each Model:")
print(summary_stats)
