#stored following word in a python dictionary
words={
    "table":["a piece of furniture"," list of facts & figure"],
    "cat":"a small animal"
}
print(words)

#you are given a list of subject for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students.
subject = {
    "python","java","c++","python","javascript","java",
    "python","java","c++","c"
}
print(subject)
print(len(subject))

#wap to enter marks of 3 subject from the user and store them in a dictionary. start with an empty dict and add one by one. use subject name as key & marks as value
marks={}
x=int(input("enter phy: "))
marks.update({"phy": x})
x=int(input("enter math: "))
marks.update({"math": x})
x=int(input("enter chem: "))
marks.update({"chem": x})
print(marks)

#figure out a way to store 9 and 9.0 as separate values in the set
value={9,"9.0"}
print(value)

#2 pairs in the form of tuple
values={
    ("float",9.0),
    ("int",9)
}
print(values)