import random

def gamewin(comp,you):
    # if two values are equal , declare a tie!
    if comp == you:
        return None

    # check all posiblites when computer choose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # check all posiblites when computer choose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    # check all posiblites when computer choose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
        

print("Comp Turn:Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    Comp ='s'
elif randNo==2:
    Comp='w'
elif randNo == 3:
    Comp = 'g'

you = input("your's Turn:Snake(s) Water(w) or Gun(g)?")
a = gamewin(Comp,you)
print(f"computer choose {Comp}")
print(f"your's choose {you}")
if a == None:
    print("The game is tie!")
elif a:
    print("you win!")
else:
    print("you loose")


