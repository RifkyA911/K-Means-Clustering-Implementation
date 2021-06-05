import numpy as np
import pandas as pd
from pandas import *

# Seleksi Kolom Pm10 dan PM25
data = read_csv("Pola K-Means\ISPU.csv")
pm10 = data['pm10']
pm25 = data['pm25']

ISPU_dataSet = {
    "Pm10": [pm10],

    "Pm25": [pm25]
}

df = pd.DataFrame(ISPU_dataSet)

# print(pm10[0])
# print(pm25[0])
# print("\n")
print(df)
# joinArray = [pm10, pm25]
# joinArray = str(pm10) + str(pm25)
# print(joinArray[1][1])
# df = pd.DataFrame(joinArray, columns=['FName', 'LName'],
#                   dtype=float)
# print(df)

# df = pd.DataFrame(joinArray, columns=["one", "two"])
# print(df)


k = 2
clusters = {}
for i in range(k):
    clusters[i] = []

# for i in range(k):
#     centroids[i] = X[i]

# for data in X:
#     euc_dist = []
#     for j in range(k):
#         euc_dist.append(np.linalg.norm(data - centroids[j]))
#     clusters[euc_dist.index(min(euc_dist))].append(data)


# def recalculate_clusters(X, centroids, k):
#     """ Recalculates the clusters """
#     # Initiate empty clusters
#     clusters = {}
#     # Set the range for value of k (number of centroids)
#     for i in range(k):
#         clusters[i] = []
#     for data in X:
#         euc_dist = []
#         for j in range(k):
#             euc_dist.append(np.linalg.norm(data - centroids[j]))
#         # Append the cluster of data to the dictionary
#         clusters[euc_dist.index(min(euc_dist))].append(data)
#     return clusters


# def recalculate_centroids(centroids, clusters, k):
#     """ Recalculates the centroid position based on the plot """
#     for i in range(k):
#         centroids[i] = np.average(clusters[i], axis=0)
#     return centroids
