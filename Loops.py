# 1while Loop
count=1
while(count<=5):
    count += 1
    print("Hello")

# count=1
while count<=5 :
    print("hello")
    count += 1
print(count)


# print no from 1 to 5
i=0
while i<=5:
    i+=1
    print(i)

print("end")

# 5 to 1
i=5
while i>=1:
    print(i)
    i-=1
print("end")


# 2.break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i +=1
print("end of loop")

nums=[1,4,9,16,25,36,49,64,81,100]
x=36
i=0
while i<len(nums):
    if (nums[i]==x):
        print("found at idx",i)
        break
    i += 1

# 3 continue
i=0
while i<=5:
    if(i==3):
        i+=1
        continue  #skip
    print(i) 
    i +=1   

# print odd no
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

#for Loop
nums=[1,2,3,4,5]
for val in nums:
    print(val)

veg=["potato","brijal","ladyfinger","cucumber"]
for val in veg:
    print(val)     

tup=(1,2,3,4,5)
for num in tup:
    print(num)

str='siddhi'
for char in str:
    print(char)


# when we use else-break
str="apnacollage" 

for char in str:
    if(char=='o'):
        print("o found")
        break

    print(char)
else:
    print("END")

# Pass statement
for i in range(5):
    pass
print("some useful work")

