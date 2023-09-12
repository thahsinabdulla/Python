a=int(input("enter a value for factorial"))
temp=a
sum=0
while (a):
    digitreminder=a%10
    print("digits are:",digitreminder)
    fact = 1
    i=1
    while i<= digitreminder:
      fact=fact*i
      i+= 1
      print(fact)
    sum=sum+fact
    a = a // 10
if temp==sum:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
