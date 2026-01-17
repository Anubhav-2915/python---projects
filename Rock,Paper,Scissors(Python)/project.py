import random
print("Enter r: rock, p: paper, s: scissors")
'''
rock: 1
paper: -1
scissors: 0
'''
computer= random.choice([1, 0, -1])
youdict= {"r": 1, "p": -1,"s": 0}
reversedict= { 1: "rock", -1: "paper", 0:"scissors"}
you= input("Enter your choice:")
you_num= youdict[you]
print("you chose: ",reversedict[you_num],"\n"  "computer chose: ",reversedict[computer])

if(you_num==computer):
    print("its a draw!!")
else:
    if(you_num==1 and computer==0):
        print("You Win!!")
    elif(you_num==1 and computer==-1):
        print("You Loose!!")
    if(you_num==0 and computer==-1):
        print("You Win!!")
    elif(you_num==0 and computer==1):
        print("You Loose!!")
    if(you_num==-1 and computer==1):
        print("You Win!!")
    elif(you_num==-1 and computer==0):
        print("You Loose!!")