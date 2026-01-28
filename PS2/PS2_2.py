import pandas as pd

data = pd.read_csv("ps2_2_data.csv",header = None)

n,p = data.shape

def dissimilarity(i,j):
    m = (data.iloc[i] == data.iloc[j]).sum()
    return (p - m)/p


print("DISSIMILARITY MATRIX")
for i in range(n):
    for j in range(n):
        res = dissimilarity(i, j)
        print(res," ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












def dissimilarity(i, j):
    m = (data.iloc[i] == data.iloc[j]).sum()
    return (p - m) / p

print("Dissimilarity Matrix:\n")

for i in range(n):
    for j in range(n):
        d = dissimilarity(i, j)
        print(f"{d:.2f}", end="  ")
    print()

