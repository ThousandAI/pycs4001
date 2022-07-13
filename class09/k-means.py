import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array(pd.read_csv("./k-means.csv"))
x1 = data[:,0]
x2 = data[:,1]

# plt.scatter(x1, x2, s=1)
# plt.show()

# k-means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, max_iter=1000, random_state=1)
np.random.shuffle(data)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)
plt.scatter(data[y_kmeans==0][:,0], data[y_kmeans==0][:,1], s = 2, color="red")
plt.scatter(data[y_kmeans==1][:,0], data[y_kmeans==1][:,1], s = 2, color="blue")
plt.scatter(data[y_kmeans==2][:,0], data[y_kmeans==2][:,1], s = 2, color="orange")
plt.show()



