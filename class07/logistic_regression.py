import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sigmoid function
"""
def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-6,6,0.01)
y = sigmoid(x)

plt.plot(x, y)
plt.show()
"""

data = pd.read_csv("./advertising.csv")
# sns.pairplot(data, hue="Clicked on Ad")
# plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
x = data[["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage", "Male"]]
y = data["Clicked on Ad"]

scaler = StandardScaler()
sc_x = scaler.fit_transform(x)

train_x, test_x, train_y, test_y = train_test_split(sc_x, y, test_size=0.2, random_state=10)
logistic = LogisticRegression()
logistic.fit(train_x,train_y)
predictions = logistic.predict(test_x)
print(confusion_matrix(test_y, predictions))