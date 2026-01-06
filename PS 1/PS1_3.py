import pandas as pd
from math import sqrt

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

data = {"Group 1": [10, 15, 17, 25, 14, 76, 89, 190, 50], 
        "Group 2": [18, 28, 5, 10, 28, 97, 156, 89, 55], 
        "Group 3": [65, 15, 48, 55, 20, 67, 187, 28, 1] }

df = pd.DataFrame(data)

for col in df.columns:
    mean_val = find_mean(df[col])
    std_val = find_std(df[col])
    print(col.upper())
    print("Mean:",mean_val)
    print("Standard Deviation:",std_val)
    print()
    