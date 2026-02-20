import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
scissors =('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

images = [rock, paper, scissors]
print("What do you choose?\n[ 0 ] ROCK\n[ 1 ] PAPER\n[ 2 ] SCISSORS: ")
choice = int(input(""))
if 0 <= choice <= 2:
        print(images[choice])
computer = random.randint(0,2)
print("Computer choice: ")
print(images[computer])
if choice == computer:
    print("It's a draw!")
elif choice == 0 and computer == 2 or choice == 1 and computer == 0 or choice == 2 and computer == 1:
    print("YOU WIN!")
else:
    print("YOU LOSE!")

