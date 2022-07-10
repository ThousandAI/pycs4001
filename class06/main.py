import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X, Y = datasets.make_regression(n_samples=1000, n_features=1, noise=10, random_state=10)

train_x, test_x, train_y, test_y  = train_test_split(X, Y, test_size=0.2, random_state=10)

regression = LinearRegression()
regression.fit(train_x, train_y)
y_p = regression.predict(test_x)
Y_pred = regression.predict(X)

print(f"evaluation MSE: {mean_squared_error(test_y, y_p)}")

plt.scatter(X[:, 0], Y, s = 3)
plt.plot(X,Y_pred, color = 'red')
plt.show()
