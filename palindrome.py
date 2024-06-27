rem=rev=0
x=int(input("Enter a number"))
num=x
while(x!=0):
 rem=x%10
 x=x//10
 rev=rev*10+rem
if num==rev:
  print("Palindrome")
else:
  print("not palindrome")


OUTPUT:
Enter a number6798
not palindrome

Enter a number454
Palindrome
