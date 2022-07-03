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
