# num=1
# flag=0
# if num<2:
#     flag=1
# else:
#     for i in range(2,num):
#         if num%i==0:
#             break
# if flag==1:
#     print("not prime")
# else:
#     print("prime")

num=int(input("enter a no: "))
if num<2:
    print("not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not prime")
            break
    else:
        print("prime no")