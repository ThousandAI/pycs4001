import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

X, Y = datasets.make_regression(n_samples=1000, n_features=1, noise=10, random_state=10)

train_x, test_x, train_y, test_y  = train_test_split(X, Y, test_size=0.2, random_state=10)


# print(inputs.shape)
# print(labels.shape)

# show graph
# plt.scatter(inputs[:, 0], labels, s=2)
# plt.show()


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

class LinearRegression:
    def __init__(self, lr, n_iters):
        self.lr = lr
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, x, y):
        # 1. initializing (w,b)
        n_samples, n_features = x.shape
        self.w = np.zeros(n_features)
        self.b = 0

        # 2.
        for i in range(self.n_iters):
            y_predicted = np.dot(x, self.w) + self.b

            dw = (1 / n_samples) * np.dot(x.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.w = self.w - self.lr * dw
            self.b = self.b - self.lr * db

    def predict(self, x):
        y_predict = np.dot(x, self.w) + self.b
        return y_predict



regression = LinearRegression(lr=0.001, n_iters=10000)
regression.fit(train_x, train_y)
y_p = regression.predict(test_x)

mse = mean_squared_error(test_y, y_p)
print("evaluation MSE:", mse)

Y_pred = regression.predict(X)
plt.scatter(X[:, 0], Y, s = 3)
plt.plot(X,Y_pred, color = 'red')
plt.show()