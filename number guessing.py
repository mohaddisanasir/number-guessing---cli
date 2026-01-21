import random

randomed = random.randint(1,100)
def hint(chance):
    if chance > randomed:
        print(f"\tthe number is less than {chance}")
    else:
        print(f"\tthe number is greater than {chance}")


def easy():
    print("easy mode selected")
    for i in range(10):
        chance = int(input("enter your guess: "))
        if chance == randomed:
            print("\tcongratulations , you got it right")
            exit()
        else:
            hint(chance)
            print("\ttry again!")
    print(f"\tyou lost , the number was {randomed}")



def medium():
    print("medium mode selected")
    for i in range(5):
        chance = int(input("enter your guess: "))
        if chance == randomed:
            print("\tcongratulations , you got it right")
            return
        else:
            hint(chance)
            print("\ttry again!")
    print(f"you lost , the number was {randomed}")


    

def hard():
    print("hard mode selected")
    for i in range(3):
        chance = int(input("enter your guess: "))
        if chance == randomed:
            print("\tcongratulations , you got it right")
            exit()
        else:
            hint(chance)
            print("\ttry again!")
    print(f"you lost , the number was {randomed}")
    



print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
mode = input("Please select the difficulty level:\nEasy (10 chances)\nMedium (5 chances)\nHard(3 chances)")
if mode == "easy":
    easy()
elif mode == "medium":
    medium()
elif mode == "hard":
    hard()
else:
    print("invalid difficulty level")


