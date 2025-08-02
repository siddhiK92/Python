info={
    "name":"siddhi",
    "learning":["python","c","java"],
    "topic":("dict","set"),
    "age":34,
    "is_Adult":True,
    "marks":98.5
}
print(type(info))
print(info["topic"])
print(info["name"])

# add/modify
info["name"]="sid" #add new value - overwrite
info["surname"]="kawade"
print(info)

#null
null_dic={}
null_dic["name"]="apnacollege"
print(null_dic)

#Nested dictonary
student={
    "name":"siddhi kawade",
    "subject":{
        "phy":97,
        "chem":98,
        "math":99
    }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])

#Dictonary Key-
student={
    "name":"siddhi kawade",
    "subject":{
        "phy":97,
        "chem":98,
        "math":99
    }
}

#myDect.keys()
print(student.keys())  #dict_keys(['name', 'subject'])
print(list(student.keys()))  #['name', 'subject']
print(len(student))  #2

#myDict.values()
print(list(student.values())) #['siddhi kawade', {'phy': 97, 'chem': 98, 'math': 99}]

#myDict.items()
print(student.items())  #dict_items([('name', 'siddhi kawade'), ('subject', {'phy': 97, 'chem': 98, 'math': 99})])
pairs=list(student.items())
print(pairs[0]) #('name', 'siddhi kawade') tuple

# myDict.get()
print(student["name"])
print(student.get("name"))  #siddhi kawade

print(student["name2"])   #error
print(student.get("name2"))  #no error -> None
print("hello")

# myDict.update()
student.update({"city":"delhi"})
print(student)   

new_dict={"city":"delhi", "age":23}
student.update(new_dict)
print(student)


