#list
marks=[45.6,67,77.9,23,78]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

# student=["sid",98,21,"pune"]
# print(student)
# print(len(student))
# student[0]="karan"
# print(student[0])
# print(student) #change

marks=[85,94,76,63,48]
print(marks[-3:-1])

#List Method
list.append
list=[2,3]
list.append(4)
print(list)

#list.sort-Asce
list1=[9,6,10]
print(list1.append(5)) #none -list not return anything
print(list1.sort()) #6,9,10
print(list1) 
#Desc
print(list1.sort(reverse=True))  #[10, 9, 6, 5]
print(list1)

fruit=["bannana","litchi","apple"]
print(fruit.sort()) #asce
print(fruit)
print(fruit.sort(reverse=True)) #desc
print(fruit)

#list.revrse
list=['a','d','e','f','c','b']
list.reverse()
print(list)

#list.insert
list=[2,1,3]
list.insert(1,5)  #[2, 5, 1, 3]
list.insert(3,5)  #[2, 1, 3, 5]
print(list)

#list.remove
list=[2,1,3,1]
list.remove(1)  #[2, 3, 1]
print(list)


# list.pop
list=[2,1,3,1]
list.pop(2) #[2, 1, 1]
print(list)