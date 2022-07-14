import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv("./train.csv")
test_data = pd.read_csv("./test.csv")
test_ids = test_data["PassengerId"]
#print(test_ids)

def clean(data):
    data = data.drop(["PassengerId", "Name", "Ticket"], axis=1)

    cols = ["SibSp", "Parch", "Fare", "Age"]
    for col in cols:
        data[col].fillna(data[col].mean(), inplace=True)

    data.Embarked.fillna("U", inplace=True)

    return data

train_data = clean(train_data)
test_data = clean(test_data)

X = train_data.iloc[:, 1:]
Y = train_data.iloc[:, 0]


print(f"train data shape: {X.shape}")
print(f"test data shape: {test_data.shape}")

concat_data = pd.concat([X, test_data], axis=0)
dummy_data = pd.get_dummies(concat_data)

dummy_train_data = dummy_data.iloc[:891, :]
dummy_test_data = dummy_data.iloc[891:, :]


from sklearn.model_selection import train_test_split

#train_x, val_x, train_y, val_y = train_test_split(dummy_train_data, Y, test_size=0.2, random_state=10)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
sc_x = scaler.fit_transform(dummy_train_data)

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

depth = []

for i in range(2,15,1):
    tree = DecisionTreeClassifier(criterion="entropy", max_depth = i, random_state=10)
    scores = cross_val_score(tree, sc_x, Y, cv=5)
    depth.append(scores.mean())

#print(depth)

final_tree = DecisionTreeClassifier(criterion="entropy", max_depth = 8, random_state=10)
final_tree.fit(sc_x, Y)


# test data

sc_test_data_x = scaler.transform(dummy_test_data)

submission = final_tree.predict(sc_test_data_x)

submission_data = pd.DataFrame({"PassengerId": test_ids.values, "Survived": submission })

submission_data.to_csv("submission.csv", index=False)