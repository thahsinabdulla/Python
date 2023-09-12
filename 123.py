print(" 1:add\n 2:sub\n 3:multi\n 4:divi\n")
c=int(input("enter the choice"))
a=int(input("enter a value"))
b=int(input("enter a value"))
if a==1:
 sum=a+b
 print("Addition of a and b is:",sum)
elif a==2:
 sub=a-b
 print("Substraction",sub)
elif a==3:
 multi=a*b
 print("Multiplication",multi)
elif a==4:
 div=a/b
 print("Divition",div)
else:
 print("invalid")
 
