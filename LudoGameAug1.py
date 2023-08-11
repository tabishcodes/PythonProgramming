import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper or scissors): ")

  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}

  return choices


def check_win(player, computer):

  print(f"You chose {player}, computer chose {computer}")

  if player == computer:
    return "It's a tie!"

  elif player == "rock":
    if computer == "scissors":
      return "You Wins!"
    else:
      return "Computer Wins!"

  elif player == "scissors":
    if computer == "paper":
      return "You Wins!"
    else:
      return "Computer Wins!"

  elif player == "rock":
    if computer == "scissors":
      return "You Wins!"
    else:
      return "Computer Wins!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)


'''…or create a new repository on the command line
echo "# PythonLearning" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/tabishcodes/PythonLearning.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/tabishcodes/PythonLearning.git
git branch -M main
git push -u origin main
'''