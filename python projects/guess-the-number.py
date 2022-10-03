import random
randomNumber=random.randint(1,100)
print(randomNumber)
 
userguess=None
guesses=0

while (userguess!=randomNumber):
    userguess = int(input("Enter your number:"))
    guesses +=1
    if (userguess==randomNumber):
        print("You guessed it right!")
    else:
        if(userguess>randomNumber):
            print("Try Again! Enter a smaller number")
        else:
            print("Try Again! Enter a Larger number")

print(f"you guesses the number in {guesses} guesses")

with open("C:\\Users\\paras\\Desktop\\python project\\hiscore.txt","r") as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print("you have just broken the high score!")
    with open ("C:\\Users\\paras\\Desktop\\python project\\hiscore.txt","w")as f:
        f.write(str(guesses))
