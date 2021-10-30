def multiplication(num):
    print("multiplication table of ",num)
    for i in range(1,11):

     print(num,"x",i,"=",num*i)

     multiplication(int(input("Enter the number")))