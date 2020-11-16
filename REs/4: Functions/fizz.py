def adigits(a,b,c):
    x1 = max(a,b,c)
    x2 = min(a,b,c)
    if (x1 == a and x2 == b) or (x1==b and x2==a):
        return x1*100 + c*10 + x2
    if (x1 == b and x2 == c) or (x1==c and x2==b):
        return x1*100 + a*10 + x2
    if (x1 == a and x2 == c) or (x1==c and x2==a):
        return x1*100 + b*10 + x2
    