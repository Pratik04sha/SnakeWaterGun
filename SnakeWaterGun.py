import random
print("S stands for Snake, G stands for Gun and W stands for Water")
print("Enter anyonne S, G or W:")
user=input()
computer=["S", "G", "W"]
computer_choice= random.choice(computer)
print("You have chosen ", user)
print("Computer has chosen ", computer_choice)

if ((user=="S" and computer_choice=="S") or (user=="G" and computer_choice=="G") or (user=="W" and computer_choice=="W") ) :
    print("It's a DRAW")
elif ((user=="S" and computer_choice=="G") or (user=="G" and computer_choice=="W") or (user=="W" and computer_choice=="S")):
    print("Computer is WINNER")
elif ((user=="S" and computer_choice=="W") or (user=="G" and computer_choice=="S") or (user=="W" and computer_choice=="G") ):
    print("You are WINNER")
else:
    print("Invalid input given....")
