# -----------------------Indexing and slicing----------------------------------------------
#Example 1
#Indexing => calling data with the help of index in group data(Data Structure) 
#------------------positive indexing-----------------

#In list
my_data = ['hello', 'world', 'python'] # => each and evey data are allocted in different memory allocation 
print(my_data[0])
print(my_data[1])
print(my_data[2])


# index value assignement
my_data[0] = 'byee'  # It will change the data of first 0th index in the group data(DS)
#=> List is mutable so, data is changeable
print(my_data)

# In set
my_data1 = {1, 2, 3, 4, 5} # onorder and there is no indexing in set (it sort the data)
# print(my_data1[1])

#In string => A group of the character
a = 'Hello World' # Immutable
print(a[0])
for i in a:
    print(i)

# In tuple
my_data3 = ('Hello', 'world', 'python')
print(my_data3[1])

#In Dictionary
my_data4 = { #=> call the data by using key
    'a':'hello',
    'p' : 'world',
    'r' : 'python'
}

print(my_data4['a'])

# Changign data in dictionary 
my_data4['r'] = 'Django' #=> It is mutable so we can change the data using key
print(my_data4)


#---------Neagative Indexing (define from last -1, -2 .....) -------------
my_data5 = ['hello', 'world', 'python']

print(my_data5[-1])

#change data with negative index
my_data5[-1] = 'Django'
print(my_data5)


#-------------------------------Slicing (calling group of index from to where it is indicated with :)--------------------------------------------
#Slicing with postitive 
my_data6 = ["hello", "world", "Python", "course", 'Django']
a = my_data5[0:2]

#To calling data individually
b, c = my_data5[0:2] # it will print first and second index only 0 and 1
print(a)
print(b, c)

# Assigning or changing the data
my_data6[0:2] = ['Byee', 'universe'] #=> change the data by slicing 
print(my_data6)

#slicing => use extra slicing index for decreasing the index while slicing
z = my_data6[3:0:-1] #=> -1 indicated how the data index go back
# it will print the data from 3rd index to 0th index in reverse order
print(z)

# slicing with negative 
b = my_data6[-3 :-1]
print(b)

c = my_data6[-1 : -3 : -1]
print(c)