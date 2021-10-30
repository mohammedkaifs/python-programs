#use open fucntion to read the content of the file

# f = open('sample.txt','r')
# data = f.read(5) #read the first 5 characters of the file
# print(data)
# f.close()


f=open('sample.txt','r')
#read first line
data = f.readline() 
print(data)
#read second line
data = f.readline() 
print(data)
f.close()