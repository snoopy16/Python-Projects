"""
Example: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
- player game
- rock beats scissor
- scissors beat paper
- paper beat rock
- input their choice, output who is the winner
"""

# Rules
dict_rules = {
    "rock": ["rock", "scissors"],
    "scissors": ["scissors", "paper"],
    "paper": ["paper", "rock"]
}

print("Rock Paper Scissor Game. Chose from the following options: rock, paper, scissors\n")
a = input("Player 1, Input your choice ").lower()

# Check to see if user inputs are valid or not
if a not in dict_rules.keys():
    print(f"Player 1, Invalid Input {a}")
    exit(0)

b = input("Player 2, Input your choice ").lower()

# Check to see if user inputs are valid or not
if b not in dict_rules.keys():
    print(f"Player 2, Invalid Input {b}")
    exit(0)

if a == b:
    print("Its a draw")
    exit(0)

for key, value in dict_rules.items():
    if a in value and b in value:
        # We now have to decide the winner
        if a == key:
            print(f"Player 1 is the winner! (Answer: {a})")
        else:
            print(f"Player 2 is the winner! (Answer: {b})")