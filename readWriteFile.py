#another way to open and close file
# with open("practice.txt") as file:
#Read a line
#print(file.readline())
#print line by line using Read line method
# line = file.readline()
# while line !="":
#     print(line)
#     line = file.readline()
#To take lines as list
# for line in file.readlines():
#     print(line)

#Write a data into a file
#Reverse the data in the file
with open("practice.txt",'r') as reader:
    data = reader.readlines()
    reversed(data)
    with open("practice.txt",'w') as writer:
        for line in reversed(data):
            writer.write(line)


