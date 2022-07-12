import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./drug200.csv")
# print(data.head(5))

x = data.iloc[:,:-1]
y = data.iloc[:,-1:]

dummy_x = pd.get_dummies(x)
# print(dummy_x)

from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(dummy_x, y, test_size=0.2, random_state=10)

print(f"train_x shape:  {train_x.shape}")
print(f"test_x shape: {test_x.shape}")

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(criterion="entropy", max_depth = 4, random_state=10)
tree.fit(train_x, train_y)
y_pred = tree.predict(test_x)

from sklearn import metrics
print("DecisionTree Accuracy: ", metrics.accuracy_score(test_y, y_pred))
