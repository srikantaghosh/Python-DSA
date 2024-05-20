import random 

roll_again = "Y"
while roll_again== "Y":
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)

    print(f"Dice1: {dice1} \nDice2: {dice2}")
    roll_again = input("Do you want to roll the dices again?(Y/N) ")






