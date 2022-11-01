# my code
from art import logo
import random

print(logo)

pc_guss=random.randint(1,100)
print("Welcome to the Number Gussing Game!" )
print("I'm thinking of a number between 1 and 100. ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :")
if difficulty == 'easy':
    i=10
    while i >0:
        user_guss=int(input(f"You have {i} attempts remainig to guss the number. "))
        i=i-1
        if pc_guss > user_guss:
            print("too low.\nGess again")
        elif pc_guss < user_guss:
            print("too high.\nGess again")
        
        elif pc_guss == user_guss:
            print("you'r guss is right ")
            break
        elif i==1:
            print("batter luck next time")
elif difficulty == 'hard':
     i=5
     while i >0:
        user_guss=int(input(f"You have {i} attempts remainig to guss the number. "))
        i=i-1
        if pc_guss > user_guss:
            print("too low.\nGess again")
        elif pc_guss < user_guss:
            print("too high.\nGess again")
        elif i==0:
            print("batter luck next time")
        elif pc_guss == user_guss:
            print("you'r guss is right ")
            break






#answer
""""from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  "checks answer against guess. Returns the number of turns remaining."
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()"""
