def readFile(filename):
    with open(filename,'r') as f:
        print(f.red())


readFile("1.txt")
readFile("2.txt")
readFile("3.txt")