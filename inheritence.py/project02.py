import random
randNumber=random.randint(1,100)

# print(randNumber)
userGuess=None
guesses = 0
while(userGuess!=randNumber):

    userGuess = int(input("Enter your guess:"))
    guesses +=1
    if(userGuess==randNumber):
       print("you guussed it right!")
    else:  
        if(userGuess>randNumber):
            print("you guussed it wrong! Enter a smaller number")
        else:
            print("you guussed it wrong! Enter a larger number")
            

print(f"you guessed the number in  {guesses}")

with open("hiscore.txt",'r') as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("you have just broken the high score!")
    with open("hiscore.txt",'w') as f:
        f.write(str(guesses))