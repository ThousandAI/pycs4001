import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
data = pd.read_csv("./advertising.csv")

x = data[["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage", "Male"]]
y = data["Clicked on Ad"]

scaler = StandardScaler()
sc_x = scaler.fit_transform(x)

train_x, test_x, train_y, test_y = train_test_split(sc_x, y, test_size=0.2, random_state=10)
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(train_x,train_y)
# predictions = knn.predict(test_x)
# print(confusion_matrix(test_y, predictions))
# print(knn.score(test_x, test_y))

train_score = []
test_score = []
for i in range(1,21):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(train_x, train_y)
    train_score.append(knn.score(train_x, train_y))
    test_score.append(knn.score(test_x, test_y))

print(f"train_score: {train_score}")
print(f"test_score: {test_score}")

x_axis = np.arange(1,21,1)
plt.scatter(x_axis, np.array(train_score), color="r", label="train")
plt.scatter(x_axis, np.array(test_score), color="b", label="test")
plt.title("KNN score")
plt.xlabel("N neighbors")
plt.ylabel("Accuracy")
plt.legend()
plt.show()