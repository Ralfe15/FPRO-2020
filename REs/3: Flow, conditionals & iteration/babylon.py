import random
num = int(input())
x0 = random.randint(0,num)
x1=0

if x0*x0 == num:
    print(x0)
else:
    x1 = (x0+(num/x0))/2
    while round(x0,2) != round(x1,2):
        x0=x1
        x1 = (x0+(num/x0))/2
    print(round(x0,2))
    