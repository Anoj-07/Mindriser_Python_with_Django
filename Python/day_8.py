# ----------------------------------Function and its parameters and Arguments ------------------------------------------------

def Hello_name(a, b):
    print(a + b)

Hello_name(20, 40) # positional arguments
Hello_name(b=40, a=20) # keyword arguments

# ------------------------------------ * args and ** kwargs in functions ---------------------------------------------------------
ram_child1 = 'ram'
ram_child2 = 'shyam'

sam_child1 = 'sam'

# Args
def Hello_name(* child): # args is a tuple (parameter)
    # print(*child) => # here *child is unpacking the tuple
    print(child)
    
Hello_name(ram_child1, ram_child2) # positional arguments
Hello_name(sam_child1) # positional arguments


# Kwargs
def Hello_name(** child): # kwargs is a dictionary (parameter) => its a key-value pair
    print(child) 
    
Hello_name(ram_child1=ram_child1, ram_child2=ram_child2) # keyword arguments


# ----------------------------------Return keyword --------------------------------------------------------------
def Hello_name(a, b):
    return a+b

print(Hello_name(20, 40)) # positional arguments
print(Hello_name(b=40, a=20)) # keyword arguments


#------------------------------------File Handling-------------------------------------------------------------
# File handling is used to read and write files in Python

# open() function is used to open a file in Python
print('======================================================================================')

# Read a file -------------------
file = open('Day_2/day_2.py', 'r') # 'r' is used to open a file in read mode
read_file = file.read() # read() function is used to read the contents of a file
file.close() # close() function is used to close the file
print(read_file) # print the contents of the file

# Write a file------------------
file = open('hello.py', 'w') # 'w' is used to open a file in write mode
 # write function is used to write the contents of a file

file.write('Hello day_2') # => must be a string
file.close()

# Append a file------------------
file = open('Hello.text', 'a') # 'a' is used to open a file in append mode
file.write('I am appending this file') # write function is used to write the contents of a file
file.close()




