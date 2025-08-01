#wap to check if a no is even or odd entered by user
num=int(input("enter a no: "))
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")


#wap to find the greatest of 3 numbers enterd by the user
num1=int(input("enter 1st no:"))
num2=int(input("enter 2nd no:"))
num3=int(input("enter 3rd no:"))
if(num1>num2 and num1>num3):
    print("no 1 is greatest number")
elif(num2>num1 and num2>num3):
    print("no 2 is greatest number")
else:
    print("no 3 is greatest number")

#wap to check if a number is a multiple of 7 or not
num=int(input("enter a no: "))
if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")