n1 = int(input())
n2 = int(input())
n2_init = n2
i=0
while True:
    if n2 < 1:
        break
    else:
        n2/=10
        i+=1
n1=(n1*(10**i))
n1 += n2_init
print(n1)