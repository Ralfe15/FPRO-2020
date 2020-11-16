n = int(input())
res = ""

for i in range(n+1):
    if i%5 == 0 and i%3 == 0:
        pass
    elif i%3 == 0:
        res+="Fizz "
    elif i%5 == 0:
        res+="Buzz "
    else:
        res+="{} ".format(str(i))
print(res)