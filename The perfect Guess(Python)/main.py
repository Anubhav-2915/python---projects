import random
a= random.randint(1,100)
n= int(input("Enter your Guess please:"))
guesses=1
while(n != a):
    guesses+=1
    if(n>a):
        n= int(input("Lower number please:"))
    elif(n<a):
        n=int(input("Higher number please:"))

print(f"You have correctly guessed the number {a} in {guesses} attempts!!")
