# Author: Thousand AI

# 註解

# 變數 Variable
"""
x = 3 # assign 賦值
y = 2.5
z = "Hello Python"
a = True
b = False

# 原生型態 Primitive type
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
"""

# Pass by reference
"""
x = 3
y = x
print(id(x), id(y))
x = x + 1
print(id(x), id(y))
z = 4
print(id(z))
"""

# 輸出 print
"""
print("Hello") # 自動換行
print("Python")

print("Hello", end=" ")
print("Python")

print("Hello", end=",")
print("Python")

print("Hello, Python.\nI'm Thousand.")
"""

# 輸出格式 (format)
"""
guest = "Allie"
host = "Thousand"

print("Hello, " + guest + ". My name is " + host + ".")
print(f"Hello, {guest}. My name is {host}.")
print("Hello, {}. My name is {}.".format(guest, host))

pi = 3.14159265
print(f"Pi is {pi:.3f}")
print("Pi is {:.3f}".format(pi))
"""

# 資料型態不同導致運算結果不同
"""
a = "123"
b = "456"
c = 123
d = 456
print(a+b)
print(c+d)
"""

# 輸入
"""
number = input("")
print(f"Your number is {number}")
print(type(number)) # string
number = int(number)
print(type(number))
"""

# 輸入時候就轉型
"""
number = int(input("Enter a number: "))
print(f"Your number is {number}")
print(type(number))
"""

# try except
"""
try:
    number = int(input("Enter a number: "))
    print(f"Your number is: {number}")
except ValueError:
    print("輸入格式錯誤，請輸入數字")
"""

# operator
"""
x = 5
y = 3
print(f"x+y={x+y}")
print(f"x-y={x-y}")
print(f"x*y={x*y}")
print(f"x/y={x/y}") # 小數點除法
print(f"x/y={x//y}") # 整數除法
print(f"x*x*x={x**3}")
print(f"x%y={x%y}")
"""

# 餘數應用
"""
num = int(input("Enter a number: "))
print(f"百位數字: {num//100}")
print(f"十位數字: {(num//10)%10}")
print(f"個位數字: {num%10}")
"""

# 交換數值
"""
x = int(input("x: "))
y = int(input("y: "))
#tem = x
# x = y
# y = tem
x,y = y,x
print(f"x: {x}, y:{y}")
"""

# 控制流程
"""
num = int(input())
if num > 200:
    print(f"{num} > 200")
else:
    print(f"{num} <= 200")
"""

# 非 0 是 True，0 是 False
"""
if 0:
    print("This is Ture")
else:
    print("This is False")
"""

# if/elif/else
"""
num = int(input())
if num > 200:
    print(f"{num} > 200")
elif 100 <= num <= 200:
    print(f"100 <= {num} <= 200")
else:
    print(f"{num} < 100")
"""

# if/elif/else vs. 多個 if
"""
num = 3
if num >= 2:
    print(f"{num} >= 2")
elif num >= 1:
    print(f"{num} >= 1")
else:
    print(f"{num} >= 0")

if num >= 2:
    print(f"{num} >= 2")
if num >= 1:
    print(f"{num} >= 1")
if num >= 0:
    print(f"{num} >= 2")
"""

# if/else 解答
"""
x = int(input())
y = int(input())
z = int(input())

if x > y:
    ans = x
else:
    ans = y

if z > ans:
    ans = z

print(f"最大值: {ans}")
"""

# Nested if
"""
n = int(input("Enter a number"))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
"""

# while 迴圈
i = 0
while i < 10:
    print(i)
    i += 1

