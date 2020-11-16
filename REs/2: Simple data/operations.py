money = float(input())
frequency = int(input())
rate = float(input())

print(round(money*((1+(rate/frequency))**(2*frequency)),3))