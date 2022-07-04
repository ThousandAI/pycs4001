# 函式
"""
def get_sum(course,*args):
    scores = sum(args)
    print(f"{course} 總分為: {scores}")

get_sum("Math",30,20,60,80,100,90,70,98)

def get_sports(sports, **kwargs):
    print(sports)
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k}: {v}")

get_sports( "basketball",curry=[15,10,5,10], thompson= [20,10,10,5] )
"""

# dictionary
"""
dic = {"sports":["basketball", "football"], "name": ["Allie", "Thousand"]}
print(dic["sports"])
print(dic["sports"][0])

# 新增 key
dic["scores"] = [70, 80, 90, 100] # 跟 list 新增方式不一樣，更為簡單
dic["hobby"] = "Reading" # value 也可以只有一個人
print(dic)

# 迴圈 + 字典

for key in dic.keys():
    print(f"key is: {key}")

for value in dic.values():
    print(f"value is: {value}")

for key, value in dic.items():
    print(f"key is: {key}, and value is: {value}")
"""

# 迴圈 + 字典 (解答)
"""
n = int(input())
dic = {}
for i in range(n):
    tem = input().split()
    if tem[0] not in dic:
        dic[tem[0]] = [int(tem[1])]
    else:
        dic[tem[0]] += [int(tem[1])]

print(dic)
"""

# sorted + 字典 (解答)
"""
dic = {"Harry":32,"Berry":31,"Thousand":21,"Becky":50,"Allie":37}
sorted_tuple = sorted(dic.items(), key=lambda item: item[1])
sorted_dic = {key: value for key, value in sorted_tuple}
print(sorted_dic)
"""

# 物件導向建構子 (Warrior)
"""
class Warrior:
    def __init__(self, name, gender, weapon="bat"):
        self.lv = 1
        self.exp = 0
        self.n = name
        self.g = gender
        self.w = weapon
        self.sp = 100
        print("This is Warrior class.")

    def __str__(self):
        return f"Name: {self.n}, Gender: {self.g}, Weapon: {self.w}, Level: {self.lv}, Exp: {self.exp}"

    def attack(self, enemy):
        self.exp += 40
        enemy.hp -= 1
        self.level_up()
        print(f"{self.n} attacked! Level: {self.lv}, Exp: {self.exp}, Enemy Hp: {enemy.hp}")

    def level_up(self):
        if self.exp >= 100:
            self.lv += 1
            self.exp -= 100


class Enemy:
    def __init__(self):
        self.name = "Monster"
        self.hp = 100

warrior1 = Warrior(name = "Thousand", gender = "Male", weapon = "Sword")
warrior2 = Warrior(name = "Allie", gender = "Female", weapon = "Longbow")
e1 = Enemy()
print(f"Warrior: {warrior1}")

for i in range(5):
    warrior1.attack(e1)
"""

# Magician
"""
class Magician:
    def __init__(self, name, gender, weapon="bat"):
        self.lv = 1
        self.exp = 0
        self.n = name
        self.g = gender
        self.w = weapon
        self.mp = 100
        print("This is Magician class.")

    def __str__(self):
        return f"Name: {self.n}, Gender: {self.g}, Weapon: {self.w}, Level: {self.lv}, Exp: {self.exp}"

    def attack(self, enemy):
        self.exp += 40
        enemy.hp -= 1
        self.level_up()
        print(f"{self.n} attacked! Level: {self.lv}, Exp: {self.exp}, Enemy Hp: {enemy.hp}")

    def level_up(self):
        if self.exp >= 100:
            self.lv += 1
            self.exp -= 100
"""

# inheritance
"""
class Character:
    def __init__(self, name, gender, weapon="bat"):
        self.lv = 1
        self.exp = 0
        self.n = name
        self.g = gender
        self.w = weapon
    print("This is Character class.")
    def __str__(self):
        return f"Name: {self.n}, Gender: {self.g}, Weapon: {self.w}, Level: {self.lv}, Exp: {self.exp}"

    def attack(self, enemy):
        self.exp += 40
        enemy.hp -= 1
        self.level_up()
        print(f"{self.n} attacked! Level: {self.lv}, Exp: {self.exp}, Enemy Hp: {enemy.hp}", end = " ")

    def level_up(self):
        if self.exp >= 100:
            self.lv += 1
            self.exp -= 100

class Warrior(Character):
    def __init__(self, name, gender, weapon="bat"):
        super().__init__(name, gender, weapon)
        self.sp = 100

    # override
    def attack(self,enemy):
        super().attack(enemy)
        #print(f"{self.n} attacked {enemy.n} with {self.w}")
        print(f"with {self.w}")

    def bash(self, enemy):
        if self.lv >= 5:
            print(f"{self.n} used bash.")
            enemy.hp -= 10
        else:
            print("等級5才能使用")

class Magician(Character):
    def __init__(self, name, gender, weapon="bat"):
        super().__init__(name, gender, weapon)
        self.mp = 100

    def fireball(self,enemy):
        if self.lv >= 5:
            print(f"{self.n} used fireball.")
            enemy.hp -= 10
        else:
            print("等級5才能使用")

class Enemy:
    def __init__(self):
        self.n = 'Monster'
        self.hp = 100

warrior1 = Warrior(name="Thousand", gender="Male", weapon="Sword")
magician1 = Magician(name="Allie", gender="Female", weapon="Wand")
e1 = Enemy()

print(warrior1)
print(magician1)

for i in range(10):
    warrior1.attack(enemy=e1) # override

warrior1.bash(enemy=e1)
magician1.fireball(enemy=e1)
"""

import numpy as np

# numpy basic
"""
a = np.array([1,2,3])
b = np.array([[1.0,2.0,3.0],[3.2,5.7,8.2]])
print(f"a: {a}")
print(f"a dimension: {a.ndim}")
print(f"a shape: {a.shape}")
print(f"a type: {a.dtype}")
print(f"b: {b}")
print(f"b dimension: {b.ndim}")
print(f"b shape: {b.shape}")
print(f"b type: {b.dtype}")
"""

# index/slice/2D
"""
a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(a[1,2]) # 8
print(a[0,:]) # [1,2,3,4,5]
print(a[:,2]) # [3,8]
print(a[0,1:5:2]) # [2,4] (start,stop,step)
a[1,2] = 20
print(a)
a[:,2] = [7,8]
print(a)
"""

# index/slice/3D
"""
a = np.array([[[1,2],[3,5],[7,8]],
              [[1,7],[-3,2],[10,2]],
              [[6,-2],[5,-3],[7,9]],
              [[8,5],[-2,2],[26,-2]],
              [[1,-7],[-3,2],[-5,-2]],])

print(a)
print(a.shape) 
print(a[3,2,0])
print(a[:,1,:])
"""

# initializing
"""
a = np.zeros((5,3,2))
b = np.ones((2,3))
c = np.ones((2,3), dtype=np.int32)
d = np.full((2,3), 100, dtype=np.float32)
print(a)
print(b,b.dtype)
print(c,c.dtype)
print(d,d.dtype)
"""

# random
"""
x = np.random.rand(3,2)
y = np.random.randint(low=10, high=100, size= (3,2))
print(x)
print(y)
"""

# 基本運算
"""
a = np.array([[1,2,3],[4,5,6]])
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)
"""

# 運算 (list vs. array)
"""
a = [1,2,3]
b = [4,5,6]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c)
print(a+b)  # 相加是串列相加

x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y) # 平行運算

"""

# 矩陣乘法
"""
a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[2,3,1],[5,2,1]])
print(np.matmul(a,b))
"""

# 乘法單位元素
"""
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
identity = np.identity(3)
print(np.matmul(a,identity))
"""

# copy
"""
a = np.array([[1,2],[3,4]])
b = a
b[0,0] = 3
print(a)
print(b)
c = a.copy()
c[0,0] = 5
c[1,0] = -1
print(a)
print(b)
print(c)
"""

# statistics
a = np.array([[92,83,56,77,98],[81,53,64,76,60]])
print(np.max(a,axis=0))
print(np.max(a,axis=1))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))