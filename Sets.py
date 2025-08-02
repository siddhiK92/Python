collection={1,2,3,4,"hello",4,4,"world"}
print(collection)
print(type(collection))
print(len(collection))

#empty set
collection1=set()  #empty set
print(collection1)
collection1={} #empty dictonary
print(type(collection1))

# set methods
#add
collecton=set()
collecton.add(1)
collecton.add(2) #int
collecton.add("siddhi") #string
collecton.add((1,2,3)) #tuple
print(collecton)
print(len(collecton))

#remove
collecton.remove(2)  #{1, 'siddhi'}
print(collecton)

#clear
collecton.clear()
print(collecton)
print(len(collecton))

#pop -remove random values
collecton={"hello","siddhi","coding","python"}
print(collecton.pop())
print(collecton.pop())

#union
set1={1,2,3,4,5}
set2={4,5,6,7,8}

print(set1.union(set2)) #{1, 2, 3, 4, 5, 6, 7, 8}
print(set1)  #{1, 2, 3, 4, 5}

#intersection
print(set1.intersection(set2))  #{4, 5}