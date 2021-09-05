import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter the number/guess: "))
    guesses += 1

    if(userGuess == randNumber):
        print("You guessed it right!")
    elif(userGuess > randNumber):
        print("You guessed it wrong, guess smaller number")
    else:
        print("You guessed it wrong, guess greater number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
