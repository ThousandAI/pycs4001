import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
train_data = pd.read_csv("https://raw.githubusercontent.com/ThousandAI/pycs4001/main/class09/train.csv")
test_data = pd.read_csv("https://raw.githubusercontent.com/ThousandAI/pycs4001/main/class09/test.csv")
test_ids = test_data["PassengerId"]

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

concat_data = pd.concat([X, test_data], axis=0)
dummy_data = pd.get_dummies(concat_data)

dummy_train_data = dummy_data.iloc[:891, :]
dummy_test_data = dummy_data.iloc[891:, :]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
sc_x = scaler.fit_transform(dummy_train_data)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

depth = []
for i in tqdm(range(2,50,1)):
  rf = RandomForestClassifier(max_depth=i)
  scores = cross_val_score(rf, sc_x, Y, cv=5)
  depth.append(scores.mean())

final_depth = np.argmax(np.array(depth)) + 2
print(final_depth)

estimator = []
for i in tqdm(range(50,200,1)):
  rf = RandomForestClassifier(n_estimators=i, max_depth=22)
  scores = cross_val_score(rf, sc_x, Y, cv=5)
  estimator.append(scores.mean())


final_rf = RandomForestClassifier(n_estimators=200, max_depth=22)
final_rf.fit(sc_x, Y)
sc_test_data_x = scaler.transform(dummy_test_data)
submission = final_rf.predict(sc_test_data_x)
submission_data = pd.DataFrame({"PassengerId": test_ids.values, "Survived": submission })
submission_data.to_csv("submission.csv", index=False)