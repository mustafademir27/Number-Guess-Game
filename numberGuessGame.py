import random
while True:
    print("\n")
    print("***NEW GAME***")
    randNum = random.randint(1,100) #random number 0-100
    guessNum = 7    ## number of guess
    while True:
        print("\n")
        if guessNum > 0:
            guess = int(input("Please guess a number in the interval 0-100 = "))
        else:
            print("You could not find the number. The right asnwer is {}".format(randNum))
            break
        if guess != randNum:
            guessNum -= 1
            if guess > randNum:
                print("The correct answer is below. You have {} guesses left.".format(guessNum))
            elif guess < randNum:
                print("The correct answer is above. You have {} guesses left.".format(guessNum))
        elif guess == randNum:
            print("Congratulations! You found out right guess.")
            break
    answer = input("Do you play again (Y/N) = ")
    if answer == "Y":
        continue
    elif answer == "N":
        print("Program is being ended.")                
        break
    
print("GAME OVER!")


        

