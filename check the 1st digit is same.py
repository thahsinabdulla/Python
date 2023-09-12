a=int(input("enter the number"))
b=int(input("enter the number"))
while a>0:
  d=a%10
  a=a//10
if d==b:
  print("Starts with",b)
else:
  print("Not starts with",b)