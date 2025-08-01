str1="This is a string."
str2='siddhikawade'
str3="""This is string"""

#concatination
str="siddhi"
str4="kawade"
final_str=str+" "+str4
print(final_str)

#length of string
length=len(str)
print(length)

#indexing
str="siddhi kawade"
print(str[2])

# str[4]="@"  #not allowed modification in python

#slicing
#positive
print(str[1:4])
print(str[5:])  #end is not define
print(str[:12])  #start is not define

#negative
print(str[-4:-1])