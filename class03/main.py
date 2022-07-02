# 雙層串列
"""
matrix = [[32, 57, 89], [59,20,66], [66,78,82], [32,89,100], [70,100,30]]
print(matrix[0])
print(matrix[2][1])
"""

# 雙層迴圈
"""
for i in range(5):
    print(f"{i}: ",end="")
    for j in range(3):
        print(f"{j}",end=" ")
    print()
"""

# 雙層迴圈 (解答1)
"""
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
"""

# 雙層迴圈 (解答2)
"""
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
"""

# 雙層迴圈 (解答3)
"""
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
"""

# 雙層迴圈 + 雙層串列
"""
matrix = [[32, 57, 89], [59,20,66], [66,78,82], [32,89,100], [70,100,30]]
row = len(matrix)
col = len(matrix[0])
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
"""

# 雙層迴圈 + 雙層串列 (解答)
"""
matrix = [[32, 57, 89], [59,20,66], [66,78,82], [32,89,100], [70,100,30]]
row = len(matrix)
row_ans = [0 for i in range(row)]
col = len(matrix[0])
col_ans = [0 for j in range(col)]

for i in range(row):
    for j in range(col):
        row_ans[i] += matrix[i][j]
        col_ans[j] += matrix[i][j]
print(f"row 總和: {row_ans}")
print(f"col 總和: {col_ans}")
"""

# 函式
"""
def show():
    print("Welcome!!")

def say_hello(name):
    print(f"Hello {name}")

def add_numbers(num1, num2):
    print(num1 + num2)

show()
say_hello(name = "Thousand")  # say_hello("Thousand")
add_numbers(num2 = 9, num1 = 3) # add_numbers(3, 9)
"""

# 函式生命週期
"""
def show():
    number = 3
    print(f"This is show function: {number}")

show()
print(number) # 由於函式的生命週期結束，在此函式內部產生的變數都會消失
"""

# 操作全域變數
"""
total = 0

def change_number():
    print(total)  # 可以看到區域變數
    total += 1 # 不能操作全域變數

change_number()
"""

# 全域變數與區域變數同名
"""
total = 3

def change_number():
    total = 5
    total += 3
    print(f"This is change_number function: {total}")

change_number()
print(f"This is main function: {total}")
"""

# call by reference
"""
num = 3

def change_number(num):
    print(id(num))
    num += 2
    print(id(num))

print(f"Before change_number function: {num}")
print(id(num))
change_number(num = num)
print(f"After change_number function: {num}")
"""

# call by reference (list)
"""
numbers = [3,2,8,10,15,18]

def change_numbers(numbers):
    numbers.append(10)

print(f"Before change_numbers function: {numbers}")
change_numbers(numbers = numbers)
print(f"After change_numbers function: {numbers}")
"""

# return
"""
def get_mean(numbers):
    total = 0
    for v in numbers:
        total += v
    return total / len(numbers)

numbers = [85, 95, 96]
ans = get_mean(numbers = numbers)
print(ans)
"""

# import
"""
import random
# import random as r
# from random import randint
sample = random.randint(1,100)
print(sample)
"""

# random 函數 (解答)
"""
import random
n = int(input())
for i in range(n):
    print(random.randint(1,100), end=" ")
"""

# lambda
"""
add = lambda x: x+3
print(add(3))
print((lambda x: x+3)(3))

mul = lambda x,y: x*y
print(mul(3,5))
"""

# filter, map, sorted
"""
numbers = [3, 50, 2, 80, 49, 10, 6]
print(list(filter(lambda x: x > 10, numbers)))
print(list(map(lambda x: x + 3, numbers)))
scores = [["Harry", 32], ["Berry", 31], ["Thousand", 21]]
print(sorted(scores, key = lambda x:x[1]))
"""

# module
"""
import utils
numbers = [30, 60, 50, 80, 100, 57, 90]
utils.say_hello(guest="Thousand")
utils.introduce(name="Thousand", age=30, gender="Male")

print(utils.get_max(numbers=numbers))
print(utils.get_distance(point1=[3,5], point2=[6,1]))

print(f"This is main.py: {__name__}")
"""

# package
import helper.show as show
import helper.calculate as calculate

numbers = [30, 60, 50, 80, 100, 57, 90]
show.say_hello(guest="Thousand")
show.introduce(name="Thousand", age=30, gender="Male")

print(calculate.get_max(numbers=numbers))
print(calculate.get_distance(point1=[3,5], point2=[6,1]))