from art import logo, vs
from game_data import data
import random

#This Function will take the user input choice and  the two random choices and compare the follower count
def compare(choice, a, b):
  # checks to see if choice is 'a'
  if choice == "a":
    # checks to see if a is greater than b
    if data[a]['follower_count'] > data[b]['follower_count']:
      # returns True if a is greater than b
      return True
    else:
      # returns False if a is not greater than b
      return False
  # checks to see if choice is 'b'
  elif choice == "b":
    # checks to see if b is greater than a
    if data[b]['follower_count'] > data[a]['follower_count']:
      # returns True if b is greater than a
      return True
    else:
      # returns False if b is not greater than a
      return False

# This function will take the user input choice and  the two random choices and compare the follower count and switch a = b

# def switch(choice, a, b):
#   if choice == "a":
#     # checks to see if a is greater than b
#     if data[a]['follower_count'] > data[b]['follower_count']:
#       # returns a if a is greater than b
#       return a
#   # checks to see if choice is 'b'
#   elif choice == "b":
#     # checks to see if b is greater than a
#     if data[b]['follower_count'] > data[a]['follower_count']:
#       # returns b if b is greater than a
#       return b

#This function will start the game.
def game():
  # variable to hold the score
  score = 0
  # prints the logo
  print(logo)
  #random number selected between zero and the length of the data list 
  a = random.randint(0, len(data) -1)
  b = random.randint(0, len(data) -1)
  # prints the first choise displaying only name, description and conutry
  print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
  #prints the vs logo
  print(vs)
  # prints the second choice displaying only name, description and conutry
  print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
  # Takes the user input choice of either 'A' or 'B'
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  #begins the looping process of if the user choice is correct or not. if the user choice is correct, it will add 1 to the score and print the score if not, it will print the final score and end the game.
  while True:
    # calls the compare function and passes the user choice and the two random numbers. if the user choice is correct, it will return true and if not, it will return false.
    if compare(choice, a, b):
      #adds one point to the score
      score += 1
      #prints score
      print(f"You're right! Current score: {score}")
      # A will equal to previous B
      a = b
      #a = switch(choice, a, b)
      # B will get a new random number
      b = random.randint(0, len(data) -1)
      #Again prints out the first choice displaying only name, description and country
      #You will notice that what is printed will be what use to be choice B. This is         because the previous B will now be choice A.
      print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
      #prints the vs logo
      print(vs)
      #prints the new second choice displaying only name, description and country
      print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
      # Takes the user input choice of either 'A' or 'B'
      choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    else:
      #if compare returns false, it will print the final score and end the game.
      print(f"Sorry, that's wrong. Final score: {score} ")
      break

game()
