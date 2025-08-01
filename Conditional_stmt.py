#if
age=21
if(age>=18):
    print("you are eligibale for vote")
    print("can drive")

#elif
light="yellow"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

#else
light="white"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

else:
    print("unknown color")



#Grade student base on marks
#marks>=90,A
#marks>=80 and <90,B
#marks>=70 and <80,C
#marks>=60 and <70,D
marks=int(input("enter a marks"))
print(marks)
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")


#Nested
age=34
if(age>=18):
    if(age>=80):
        print("you can not drive")
    else:
        print("you can drive")
else:
    print("you can not drive")