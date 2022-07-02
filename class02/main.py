# for 迴圈
"""
for i in range(0,10,1):
    print(i)

# for i in range(10):
#    print(i)

"""

"""
# for 迴圈解答 (1)
n = int(input())
for i in range(1,n+1,1):
    print(i)
"""

# for 迴圈解答 (2)
"""
n = int(input())
for i in range(n,-1,-1):
    print(i)
"""

# for 迴圈解答 (3)
"""
n = int(input())
ans = 0
for i in range(1,n+1,1):
    ans = ans + i # ans += i
print(ans)
"""

# for 迴圈解答 (4)
"""
n = int(input())
ans = 0
for i in range(n):
    temp = int(input())
    ans += temp
print(ans)
"""

# 無窮迴圈
"""
i = 1
while True:
    print(i)
"""

# break
"""
x = 0
while x <= 10:
    x += 1
    if x == 3:
        break
    print(x)
"""

# continue
"""
x = 0
while x <= 10:
    x += 1
    if x == 3:
        continue
    print(x)
"""

# break (解答)
"""
ans = 0
count = 0
while True:
    x = input()
    if x == 'q' or x == 'Q':
        break
    ans += int(x)
    count += 1
print(f"總和: {ans}")
print(f"平均: {ans/count:.2f}")
"""

# 串列 list
"""
numbers = [3, 5, 6, 10, 2, 8]
cat = ["cookie", 2, 3.2]
"""

# index && slice
"""
numbers = [3, 5, 6, 10, 2, 8]
print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-3])
print(len(numbers))
print(numbers[1:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[2:-1])
print(numbers[-1:-4])
print(numbers[-3:])
print(numbers[:])
"""

# 串列 methods
"""
numbers = [3, 5, 6]
numbers.insert(2, 8)
print(f"After insert: {numbers}")
numbers.append(8)
print(f"After append: {numbers}")
numbers.remove(8)
print(f"After remove: {numbers}") # 移走第一個
numbers.sort() # 由小到大
print(f"After sort: {numbers}")
numbers.reverse()
print(f"After reverse: {numbers}")
numbers.pop()
print(f"After pop: {numbers}")
"""

# 串列 assign 記憶體問題
"""
num1 = [1, 2, 3, 4, 5]
num2 = num1
num1.append(6)
print(f"num1: {num1}, num2: {num2}")
num3 = num1[:]
num4 = num1.copy()
num1.append(7)
num3.append(8)
print(f"num1: {num1}, num2: {num2}, num3: {num3}, num4: {num4}" )
"""

# 迴圈 + 串列
"""
numbers = [3, 5, 6, 10, 2, 8]
for i in range(len(numbers)):
    print(numbers[i], end = " ")
print() # 換行
# 由右到左
for i in range(len(numbers)-1,-1,-1):
    print(numbers[i], end = " ")
"""

# python 風格寫法
"""
numbers = [3, 5, 6, 10, 2, 8]
for v in numbers:
    print(v, end=" ")
print()

# enumerate
for i, v in enumerate(numbers):
    print(f"index: {i}, value: {v}")
"""

# 迴圈 + 串列 (解答)
"""
n = int(input())
ans = []
for i in range(n):
    temp = int(input())
    ans.append(temp)
print(f"總和: {sum(ans)}, 最小值: {min(ans)}, 最大值: {max(ans)}")
"""

# 字串
"""
name = "Thousand"
print(name[0])
print(len(name))
name = name.lower() # 記得 assign 回去
print(name)
name = name.upper()
print(name)
print(name[0].islower())
print(name[0].isupper())
"""

# 字串 split
"""
s = input() # 3 5 6 10 2 8
print(s.split()) #["3", "5", "6", "10", "2", "8"]
s = input() # 3,5,6,10,2,8
print(s.split(",")) #["3", "5", "6", "10", "2", "8"]
"""

# 迴圈 + 字串 (解答1)
"""
s = input()
s = s.split()
ans = []
for v in s:
    ans.append(int(v))
print(ans)
"""

# 迴圈 + 字串 (解答2)
"""
s = input()
count = 0
for v in s:
    if v == "a":
        count += 1
print(count)
"""

# 列表推導式 list comprehension

# 產生 [0,1,2,3,4,5]
"""
ans = []
for i in range(6):
    ans.append(i)

ans = [i for i in range(6)]
print(ans)

# 產生 [0,2,4,6,8,10,12,14,16,18,20]
res = []
for i in range(21):
    if i %2 == 0:
        res.append(i)

res = [i for i in range(21) if i % 2 == 0]
print(res)
"""