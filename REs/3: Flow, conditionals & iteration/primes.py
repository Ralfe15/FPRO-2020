number = int(input())
if number < 2:
    print("False")
for i in range(2,number):
    if number%i==0:
        print("False")
        break
else:
    print("True")