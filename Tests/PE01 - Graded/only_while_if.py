a = int(input())
b = int(input())

i = a

while i < b:
    n = i
    if i**2 > (b/2)**2:
        i = b
    if not i**2 > (b/2)**2:
        if i%3 == 0 and i%5 == 0:
            i+=0
        if i%3 != 0 or i%5 != 0:
            if i%2 == 0:
                j = 0
                while j < 3:
                    n //= 2
                    j+=1
                print(n)
            if not i%2 == 0:
                n+=1
                print(n)
    i+=3