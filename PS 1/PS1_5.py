import pandas as pd
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

def find_mean(data):
    sum_num = 0
    n = len(data)
    for num in data:
        sum_num += num
    
    average = sum_num / n
    return round(average,2)

def find_std(data):
    mean = find_mean(data)
    temp_sum = 0
    n = len(data)
    for num in data:
        temp_sum += (num - mean)**2
        
    std_dev = sqrt(temp_sum/n)
    return round(std_dev,2)


data = {
        "Group 1": np.random.randint(18, 60, 15),
        "Group 2": np.random.randint(20, 65, 15),
        "Group 3": np.random.randint(25, 70, 15),
        "Group 4": np.random.randint(30, 75, 15)
}

df = pd.DataFrame(data)

df_sorted = df.apply(sorted)

for col in df_sorted.columns:
    clean_data = df_sorted[col]
    
    print(col.upper())
    print("Q1 (25%):", np.percentile(clean_data, 25))
    print("Q2 (Median):", np.percentile(clean_data, 50))
    print("Q3 (75%):", np.percentile(clean_data, 75))
    print("Mean:", find_mean(clean_data))
    print("Standard Deviation:", find_std(clean_data))
    print()


#Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data = df_sorted)
plt.title("Boxplot of Customer Age for Each Transaction Group")
plt.ylabel("Age")
plt.show()

#Histograms
plt.figure(figsize=(12, 8))
for col in df_sorted.columns:
    plt.hist(df_sorted[col], bins=7, alpha=0.6, label=col)

plt.title("Histogram of Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()