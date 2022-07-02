def say_hello(guest):
    print(f"Hello {guest}")

def introduce(name, age, gender):
    print(f"My name is: {name}")
    print(f"My age is: {age}")
    print(f"My gender is: {gender}")

def get_max(numbers):
    return max(numbers)

def get_distance(point1, point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**(1/2)

#print("Hello This is utils.py")

if __name__ == "__main__":
    print("Hello")
    print("Hello This is utils.py")