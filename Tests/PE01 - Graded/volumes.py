import math

shape = input()
radius = float(input())

if shape == "cylinder" or shape == "cone":
    height = float(input())
    if shape == "cylinder":
        print(round(height*math.pi*radius**2,1))
    else:
        print(round((1/3)*math.pi*radius**2*height,1))
elif shape == "sphere":
    print(round((4/3)*math.pi*radius**3,1))