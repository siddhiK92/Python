tuple=(2,1,3,1)
print(tuple)
print(tuple[0])
tuple[0]=5 #tuple does not support modification

tup=()
print(tup)
print(type(tup))

tup1=(1,)  #tup1=(1)
tup1=(1)   #int
tup1=(1.0)  #float
print(tup1)
print(type(tup1))

tup2=(1,2,3,)
print(type(tup2))

#Methods of tuple
tup=(2,1,3,1,1,1)
print(tup.index(1)) #1
print(tup.count(1)) #4