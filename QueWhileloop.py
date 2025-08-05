#print nos from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

print("done")


#print nos from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#print multiplication table of no n

n=int(input("Enter a no: "))
i=1
while i<=10:
    print(n*i)
    i+=1

#print the element following list
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx += 1

heros=['ironman','thor','superman','batman']
idex=0
while idex<len(heros):
    print(heros[idex])
    idex += 1

# search for a number x in the tuple using loop 
nums=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
while idx<len(nums):
    if(nums[idx] == x):
        print("fount at index",idx)
    idx += 1