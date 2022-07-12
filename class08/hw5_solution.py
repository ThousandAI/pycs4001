import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("./Salary_Data.csv")
x = np.array(data["YearsExperience"]).reshape(-1,1)
y = np.array(data["Salary"]).reshape(-1,1)

scaler = StandardScaler()
sc_x = scaler.fit_transform(x)
sc_y = scaler.fit_transform(y)

train_x, test_x, train_y, test_y  = train_test_split(sc_x, sc_y, test_size=0.2, random_state=10)

regression = LinearRegression()
regression.fit(train_x, train_y)
y_p = regression.predict(test_x)
print(f"evaluation MSE: {mean_squared_error(test_y, y_p)}")
Y_pred = regression.predict(sc_x)
Y_inv_pred = scaler.inverse_transform(Y_pred)

plt.scatter(x, y, s =3)
plt.plot(x, Y_inv_pred, color="red")
plt.show()