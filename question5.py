#write a program to find if the given number is prime no or not
num=int(input("enter the number"))
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not")            