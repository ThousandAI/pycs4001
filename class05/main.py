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
# print(data.describe())
# print(data.sort_values(["HP"], ascending=True))

data["Total"] = data.iloc[:, 4:10].sum(axis=1)
print(data)

data = data.drop(columns=["#"])
print(data)

# to csv
data.to_csv("new_pokemon.csv", index=False)
