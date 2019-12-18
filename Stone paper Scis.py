import time
import random
key='Y'
print("%80s"%("*"*34))
sleep=time.sleep(1)
print("%80s"%("**  WELCOME TO RO-SHAM-BO GAME  **"))
sleep=time.sleep(1)
print("%80s" %("*" *34))
sleep=time.sleep(1)
print("Rock-Paper-Scissor is a game in which you have to choose the one of the following Weapon \nROCK\nPAPER\nSCISSOR \nThe one with storonger Weapon wins the Battle")
sleep=time.sleep(4)
print("\n\nPOWER OF WEAPONS :\nRock wins over Scissor\nPaper wins over Rock\nScissor wins over Paper")
sleep=time.sleep(4)
print("\nLet's Begin The game",end="")
for n in range(6):
    sleep=time.sleep(0.5)
    print(".",end="")
while(key=='Y'):
    for m in range(1,11):
        for n in range(6):
            sleep = time.sleep(0.5)
            print(".", end="")
        inp=str(input("\n\nYour Chance[Rock(1),Paper(2),Scissor(3)]:"))
        R='Rock'
        P='Paper'
        S='Scissor'
        y=random.randint(1,3)
        if(y==1):
            y=R
            print('\n\nComputer Choice is %s'%(y))
        if(y==2):
            y=P
            print('\n\nComputer Choice is %s'%(y))
        if(y==3):
            y=S
            print('\n\nComputer Choice is %s'%(y))
        if((int==1 and y==2)or(int==2 and y==1)):
            win='Paper'
        elif((int==3 and y==1)or(int==1 and y==3)):
            win='Rock'
        elif((int==2 and y==3)or(int==3 and y==2)):
            win='Scissor'
        else:
            win='Draw'
        if (win==int):
            print("You Won the Battle")
        else:
            print("Computer Wins the Battle")