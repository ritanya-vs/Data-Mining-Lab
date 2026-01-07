import numpy as np
from math import sqrt 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
    "Group 1": pd.Series(np.random.normal(loc=50, scale=10, size=10)),   #loc => mean ; scale => deviation
    "Group 2": pd.Series(np.random.normal(loc=60, scale=15, size=25)),
    "Group 3": pd.Series(np.random.normal(loc=70, scale=20, size=30)),
    "Group 4": pd.Series(np.random.normal(loc=80, scale=25, size=40))
}

print("Data")
print(data)

df = pd.DataFrame(data)

for col in df.columns: 
    clean_data = df[col].dropna()
    mean_val = find_mean(clean_data) 
    std_val = find_std(clean_data) 
    print(col.upper()) 
    print("Mean:", mean_val) 
    print("Standard Deviation:", std_val) 
    print() 
    
plt.figure(figsize=(10,6)) 
for col in df.columns: 
    sns.kdeplot(df[col].dropna(), label=col, fill=True, alpha=0.3) 
    
plt.title("Bell Curves for Each Group") 
plt.xlabel("Values") 
plt.ylabel("Density") 
plt.legend() 
plt.show()
print() 
