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

a = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

b = [rock, paper, scissors]

c = int(a)
print(b[c])

import random
d = random.randint(0, 2)
print(b[d])

if c == d:
  print("It's a draw")
elif c == 0 and d == 2:
  print("You win")
elif c == 2 and d == 0:
  print("You lose")
elif c < d:
  print("You lose")
else:
  print("You win")