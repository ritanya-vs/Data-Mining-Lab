import pandas as pd
import numpy as np

data = {
    'A1': [1, 2, 3, 4, 5],
    'A2': [2, 3, 4, 5, 6],
    'A3': [3, 4, 5, 6, 7],
    'A4': [4, 5, 6, 7, 8]
}

df = pd.DataFrame(data)
print("Data Matrix:")
print(df)

n = len(df)

#distance matrix
distance_matrix = pd.DataFrame(np.zeros((n, n)))

for i in range(n):
    for j in range(n):
        distance_matrix.iloc[i, j] = np.linalg.norm(df.iloc[i] - df.iloc[j])

distance_matrix.index = df.index
distance_matrix.columns = df.index

print("\nEuclidean Distance Matrix:")
print(distance_matrix)

#similarity matrix
similarity_matrix = pd.DataFrame(np.zeros((n, n)))

for i in range(n):
    for j in range(n):
        v1 = df.iloc[i].values
        v2 = df.iloc[j].values
        similarity_matrix.iloc[i, j] = np.dot(v1, v2) / (
            np.linalg.norm(v1) * np.linalg.norm(v2)
        )

similarity_matrix.index = df.index
similarity_matrix.columns = df.index

print("\nCosine Similarity Matrix:")
print(similarity_matrix)
