file = open('practice.txt')
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
for line in file.readlines():
    print(line)

#Write a data into a file


file.close()