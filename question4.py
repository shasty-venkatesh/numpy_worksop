#write a program to find the sum of digits of a given number'
num=int(input("enter the number"))
s=0
while num!=0:
    r=num%10
    s=s+r
    num=num//10
print(s)    