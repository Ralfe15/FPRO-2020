import math

def get_len(num):
    len_n = 0
    while num>=10:
        len_n += 1
        num /=10
    len_n+=1
    return len_n
    

def sum_line(num):
    len_num = get_len(num)
    soma = 0
    for i in range(len_num-1):
        soma*=10
        tmp = num%pow(10,len_num-1)
        x1 = (num//pow(10,len_num-1))
        x2 = (tmp//pow(10,len_num-2))
        soma += math.ceil((x1+x2)/2)
        num = tmp
        len_num = get_len(num)
    return soma

def digits_average(n):
    if n < 10:
        return n
    else:
        res = sum_line(n)
        while res >= 10:
            res = sum_line(res)
        return res