num = int(input())
result = 0

while num > 0:
    temp = num%10
    result = (10*result) + temp
    num = num//10
print(result)
    