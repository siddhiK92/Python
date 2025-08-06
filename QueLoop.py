# #print nos from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# print("done")


# #print nos from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

# #print multiplication table of no n

# n=int(input("Enter a no: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# #print the element following list
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx += 1

# heros=['ironman','thor','superman','batman']
# idex=0
# while idex<len(heros):
#     print(heros[idex])
#     idex += 1

# # search for a number x in the tuple using loop 
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# idx=0
# while idx<len(nums):
#     if(nums[idx] == x):
#         print("fount at index",idx)
#     idx += 1

#using for loop
#print the elements of the following list using a loop
# nums=[1,4,9,16,25,36,49,64,81,100]
# for i in nums:
#     print(i)

#search for a no x in this tuple using loop
#linear search-single line - one by noe
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=49
# idx=0
# for i in nums:
#     if(i == x):
#         print("number found",idx)
#     idx += 1

#wap to find sun of first n natural no
# n=int(input("Enter a no:"))
# sum=0
# i=1
# while i<=n:
#     sum += i
#     i += 1
# print(sum)

#print factorial

n=5
fact=1

for i in range(1, n+1):
    fact *= i

print("factorial :",fact)
