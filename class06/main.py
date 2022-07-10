import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("./Salary_Data.csv")

scaler  = StandardScaler()
scaler .fit(data)
sc_data = scaler.transform(data)

# print(sc_data)
"""
print(sc_data[:, 0].mean())
print(sc_data[:, 0].std())
print(sc_data[:, 1].mean())
print(sc_data[:, 1].std())
"""


train_x = np.array(data["YearsExperience"])
train_y = np.array(data["Salary"])
# train_x = np.array(sc_data[:,0])
# train_y = np.array(sc_data[:,1])

plt.scatter(train_x, train_y, color="red", s=10)
plt.title("Salary & Years")
plt.show()