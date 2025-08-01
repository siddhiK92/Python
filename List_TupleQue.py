#wap to ask user to enter names of their 3 favorite movies & store them in a list
movies=[]
movie1=input("Enter 1st movie: ")
movie2=input("Enter 1st movie: ")
movie3=input("Enter 1st movie: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#wap to check if a list contains a palindrome of elements.(hint:use copy() method())
list1=[1,2,1]
# list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("List is a palindrome")
else:
    print("List is not a palindrome")

#wap to count the number of students with the "A" grade in the following tuple
grade=["c","D","A","A","B","B","A"]
print(grade.count("A"))
grade.sort()
print(grade)