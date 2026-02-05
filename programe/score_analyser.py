import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create a dummy dataset (Fundamentals of Data Creation)
data = {
    'Student_ID': np.arange(1, 11),
    'Math_Score': [85, 90, 78, 92, 88, 76, 95, 89, 84, 82],
    'Science_Score': [88, 85, 80, 95, 82, 70, 98, 91, 80, 85]
}

# 2. Load into a DataFrame (The Pandas core)
df = pd.DataFrame(data)

# 3. Data Analytics Logic
print("--- Basic Statistics ---")
print(df.describe()) # Shows Mean, Median, Min, Max

# Calculate a new column (Feature Engineering)
df['Average'] = (df['Math_Score'] + df['Science_Score']) / 2

# 4. Data Visualization (The Graph Plotter)
plt.figure(figsize=(10, 5))
sns.lineplot(x='Student_ID', y='Average', data=df, marker='o', label='Average Score')

plt.title('Student Performance Analytics')
plt.xlabel('Student ID')
plt.ylabel('Average Score')
plt.grid(True)
plt.show()
