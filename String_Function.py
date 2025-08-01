str="i am Studing Python"
#str.endswith
print(str.endswith("app"))

#str.capitalize
print(str.capitalize()) #first letter capital
print(str) #no change in original- string

#modification
# if we want original string modify
str=str.capitalize()
print(str)

#str.replace
print(str.replace("i","o"))
print(str.replace("Python","java"))

#str.find
str1="i am studing python , i am"
print(str1.find("am"))  #start from 2nd index
print(str1.find("yes"))  #invalid -1

#str.count
print(str1.count("am"))