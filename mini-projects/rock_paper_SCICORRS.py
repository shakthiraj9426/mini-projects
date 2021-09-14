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

game_images = [rock,paper,scissors]

user_input = int(input("what you choose ?. ROCK(0), PAPER(1), SCISSORS(2) : "))
print(game_images[user_input])

computer_input = random.randint(0,2)
computer_choice = game_images[computer_input]
print(f"computer chose :\n {computer_choice}")

if user_input >= 3 or computer_input < 0:
    print("you typed a invalid number, you lose")

elif user_input == computer_input:
    print("it's a draw !")

elif user_input == 0 and computer_input == 2:
    print("you win !")

elif computer_input == 0 and user_input == 2:
    print("you lose !")    

elif computer_input > user_input:
    print("you lose !")
    
elif user_input > computer_input:
    print("you win !")