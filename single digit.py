num=int(input("enter a number"))
sum=0
sum1=0
sum2=0
while num>0:
     digitseperate=num%10
     print("digits are:", digitseperate)
     sum=sum+digitseperate
     num = num // 10
print("sum is:",sum)
while sum>0 :
     sumseperate=sum%10
     print("sum seperated digits are:", sumseperate)
     sum1=sum1+sumseperate
     sum=sum//10
print("sum of sum seperated is: ", sum1)
while sum1>0 :
     sum1seperate=sum1%10
     print("sum1 seperated digits are:", sum1seperate)
     sum2=sum2+sum1seperate
     sum1=sum1//10
print("sum of sum1 seperated is: ", sum2)