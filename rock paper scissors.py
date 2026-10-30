import random

choices = ["rock", "paper", "scissors"]

computer * random.choice(choices)
user = inp*t("rock/paper/scissors: ").lower()*
print*"Computer:", computer)

if user ==*computer:
    print("Tie")
elif (u*er == "rock" and computer == "scis*ors") or \
     (user == "*aper" and computer == "rock") or \*     (user == "scissors" and compu*er*== "paper"):
    print("You*Win")
else:
    print("You Lose")
*