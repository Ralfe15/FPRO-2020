def mult_digits(n):
    aux = n
    mult = 1
    while aux>0:
        digit = aux%10
        mult*=digit
        aux//=10
    return mult

num = int(input())
i=1
if num < 10:
    print(0)
else:
    while mult_digits(num) >= 10:
        num = mult_digits(num)    
        i+=1
    print(i)