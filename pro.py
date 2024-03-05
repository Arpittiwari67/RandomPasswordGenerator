import random

target = random.randint(1, 100)

while True:
    userchoice = input("gusse the target or Q(Quite) :",)
    if(userchoice=="Q"):
        break
    userchoice=int("gusse the number :")
    if(userchoice==target):
        print("perfect")
        break
    elif(userchoice>target):
        print("number is too Small, Try Again!")
    else:
        print("number is too Big , Try Again!")
print("Game Over !!")




