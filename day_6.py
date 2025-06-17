# Data type  methods 
"""
This script demonstrates various methods associated with Python data types.
"""
#------------------------String methods----------------------------------------------------
a = 'Hello world' # it remain same 

# but it create a copy of an orginal data in upper case
print(a.lower())
print(a.upper()) 

b = '12345'
print(b.capitalize())
print(b.isdigit())

print(a.count('o')) #some methods need to pass values 


#-------------------------List Method--------------------------------------------------------
z = ['hello', 'world', 'python']
z.append('Django')
print(z)

# z.reverse()
# print(z)

z.pop(0)
print(z)

# print(z.append('Django')) => it will give you output as none

z.clear()
print(z)

#--------------------------Tuple Method---------------------------------------------------------
t = (1, 2, 3, 3, 5, 6, 7, 7, 7)

print(t.count(7))
print(t.index(3))

# to use extra method convert tuple into list
s = list(t)
print(s)

#--------------------------set Method------------------------------------------------------------
a = {1, 2, 3, 4, 5, 6, 7}
b = {4, 5, 6, 7, 8, 9}

# c = a.difference(b) # shortcut a - b
# print(c)
# print(a)

# a.difference_update(b)
# print(a)

c = a.intersection(b)
print(c)

#------------------------Dictionary Methoo---------------------------------------------------------
a = {
    'a': 'world',
    'b':'hello'
}

b = a.get('a')
print(b)

b = a.copy()
print(b)

a.pop('a')
print(a)



#----------------------------Task--------------------------------------------
# a=['Hello', 'world', 'Python', 'course', 'Django']
# for i in a:
#     print(i)

#-------------Today task outPut
a = ['Hello', 'world', 'Python', 'course', 'Django']
list(map(print, a))