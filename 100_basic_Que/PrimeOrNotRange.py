start=int(input("enter starting no:"))
end=int(input("enter ending no: "))
for num in range(start,end+1):
    if num<2:
        continue
    for i in range(2,num):
        if num%i==0:
            break

    else:
        print(num)
