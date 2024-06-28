# File I/O in python
# Reading and Writing Files
# Method or function for File 
# open() - open a file
# read() - read the contents of a file
# readline() - read at a line at a time
# readlines() - read the file line by line into a list
# write() - write strin to the file
# writelines() - write the sequences of string to the file
# close() - close the file
# with statement - open a file and close it automatically
# seek() - move the read/write location of the file pointer
# tell() - get the current location of the file pointer
# r - read mode
# w - write mode
# a - append mode
# r+ - read and write mode
# rb - read binary mode
# wb - write binary mode
# ab - append binary mode
# rb+ - read and write binary mode
# wb+ - write binary mode
# ab+ - append binary mode
# rb+ - read and write binary mode
# x - create a new file and open it for writing
# x+ - create a new file and open it for reading and writing

# f=open("practice.txt","r") # Syntax for to read and write or perform other functions in file
# data=f.read()
# print(data)

#With syntax
with open("practice.txt","w") as f:
  f.write("Hi Everyone\n"
          "we are learning Files I/O\n"
          "using Java\n"
          "I like programming in Java\n"
          )

with open("practice.txt","r") as f:
   data=f.read()
   
new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
   f.write(new_data)

