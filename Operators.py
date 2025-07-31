# arithmetic op
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

# relational/comparison op
a=50
b=30
print(a == b) #False
print(a != b) #True
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# Assignment op
num = 10
num = num + 10   #num += 10
num -= 5
num /= 5
num %=5  
num **=5
print(num)

# Logical op
a1=8
b1=5
print(not False) #True
print(not True) #False
print(not(a1>b1)) #false  8>5

val1=True
val2= False
print("AND op: ",val1 and val2)
print("OR op: ",val1 or val2)
print("OR op: ",(a1>b1) or (a1==b1) )