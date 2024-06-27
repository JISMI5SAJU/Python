def prime(num):
 for i in range (2,num):
  if num%i==0:
        return(1)
  return (0)
num=int(input("Enter number"))
s=prime(num)
if s==0:
    print("Prime")
else:
    print("Not prime")

    
