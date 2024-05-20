# find if the given number is a palindrome or not?
num=int(input("enter the number"))
print("palindrome") if str(num)[::-1]==str(num) else print("not palindrome")