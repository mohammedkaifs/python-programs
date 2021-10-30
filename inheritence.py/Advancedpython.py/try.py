while(True):
    print("press q to qiuit")
    a = input("Enter your number")
    if a=='q':
        break
    
    try:
        a= int(a)
        if a>6:
            print("you have enterd the number greater than 6")
    except Exception as e:
        print(f"your input resulted an error:{e}")

print("Thanks for playing this game ")

