#rock ,paper ,scissors game 
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
items=[0,1,2]
item=[rock,paper,scissors]
print("*"*25)
player=input("What is your name? : ")
print(f"Welcome {player} to rock paper scissors game") 
print("*"*25)
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.choice(items)
print(item[choice])
print("Computer choice :")
print(item[computer_choice])
if choice==0 and computer_choice==2:
    print("You win")
elif choice==1 and computer_choice==0:
    print("You win")
elif choice==2 and computer_choice==1:
    print("You win")
elif choice==computer_choice:
    print("No winner")
else:
    print("computer wins")