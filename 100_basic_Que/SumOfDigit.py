no=int(input("enter a no: "))
sum=0
while no!=0:
    digit=int(no%10)
    sum=sum+digit
    no=no/10
print(sum)

