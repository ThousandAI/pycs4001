import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# DataFrame
"""
dic = {"Sports":["Basketball", "Soccer", "Tennis", "Volleyball", "Badminton"],
       "Fruits":["Watermelon", "Banana", "Apple", "Lemon", "Strawberry"],
       "Animals": ["Monkey", "Ape", "Dog", "Cat", "Lion"]}


data = pd.DataFrame(dic)
print(type(data))
print(data)

# series
new_data = data["Sports"]
print(type(new_data))
print(new_data)

# 新增
data["Name"] = ["Thousand", "Allie", "John", "Michale", "Frank"]
print(data)

# 取值
print(data.iloc[1:4, 1:3])
"""

# Read file
data = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv")

# 取值
"""
# 取前五個值
# print(data.head(5))

# 取最後五個值
# print(data.tail(5))

# 取出 column 名稱
# print(data.columns)

# 取出 Name 的前3個 row
# print(data["Name"][:3])

# 取出多個 column
# print(data[["Name", "HP", "Attack"]])

# Read row
# print(data.iloc[0:5, 1:3])
# print(data.iloc[0,1])

# 找尋 HP > 50
# print(data.loc[data["HP"] > 50])
"""

# Describing / Sorting / Sum / Drop
"""
# print(data.describe())
# print(data.sort_values(["HP"], ascending=True))
 
# data["Total"] = data.iloc[:, 4:10].sum(axis=1)
# print(data)

# data = data.drop(columns=["#"])
# print(data)

# to csv
# data.to_csv("new_pokemon.csv", index=False)
"""

# Filtering
"""
# print(data.loc[(data["Type 1"] == "Fire") & (data["Type 2"] == "Flying")])

# print(data.loc[(data["Type 1"] == "Fire") | (data["Type 2"] == "Flying")])

new_data = data.loc[(data["Type 1"] == "Fire")]
print(new_data)
new_data = new_data.reset_index(drop=True)
print(new_data)
"""

# groupby
"""
# print(data.groupby(["Type 1"]).mean())
# print(data.groupby(["Type 1"]).std())
# print(data.groupby(["Type 1"]).sum())
"""

# matplotlib

"""
x = np.array([1, 2, 3, 4, 5, 6])
y = 2*x + 3

y2 = x**2

plt.plot(x, y, label='A', color = 'red', marker = '*', markersize = 10, linestyle = '--')
plt.plot(x, y2, label = 'B', color = 'blue')
plt.title("pycs4001 First Figure", fontdict={'fontname': 'Arial Black', 'fontsize': 16})
plt.xlabel("X label", fontdict={'fontname': 'Arial'})
plt.ylabel("Y label", fontdict={'fontname': 'Arial'})

# plt.xticks([0,1,2,3])
# plt.yticks([0,2,4,6,8,10])
plt.legend()
plt.savefig("pycs4001-01.png")
plt.show()
"""

# hist
"""
x = np.random.normal(0, 1, 10000)
plt.hist(x, bins=100)
plt.title("Gaussian Distribution", fontdict={'fontname': 'Arial Black', 'fontsize': 16})
plt.xlabel("x range", fontdict={'fontname': 'Arial'})
plt.ylabel("Times", fontdict={'fontname': 'Arial'})
plt.savefig("pycs4001-02.png")
plt.show()
"""

# scatter

dummy1 = np.random.multivariate_normal(mean = [-2,2], cov = [[1,0],[0,1]], size=2000)
dummy2 = np.random.multivariate_normal(mean = [2,-2], cov = [[1,0],[0,1]], size=2000)

plt.scatter(dummy1[:,0], dummy1[:,1], s = 2, label = 'A')
plt.scatter(dummy2[:,0], dummy2[:,1], s = 2, label = 'B')
plt.legend()
plt.savefig("pycs4001-03.png")
plt.show()