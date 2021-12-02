import random
import os
import hangman_words

def clear_console():
  os.system('clear')

stages = ['''
____
|  |
|  0
| /|\\
| / \\''','''
____
|  |
|  0
| /|\\
| /''','''
____
|  |
|  0
| /|\\
|''','''
____
|  |
|  0
| /|
|''','''
____
|  |
|  0
|  |
|''','''
____
|  |
|  0
|
|''','''
____
|  |
| 
|
|''']
#St1 

def pointer_creator(str, letter):
  pointer = ""
  for i in range(len(str)):
    if str[i] != letter:
      pointer += " "
    else:
      pointer += "^"
  print(pointer)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = hangman_words.word_list[random.randint(0, len(hangman_words.word_list) - 1)]

#giving player 6 lives
lives = 6
guess = " "
repeated_guess = False
guessed_letters = ""
#creating a blank word
blank_word = ""
gameover = False
word_length = len(chosen_word)
for letter in range(word_length):
  blank_word += "_"

#Beginning the primary game loop
while not gameover:
  pointer = ""
  valid_entry = False
  while valid_entry == False:
    clear_console()
    if guessed_letters != "":
      print(guessed_letters)
      if guessed_letters.find(guess) != -1 and repeated_guess == True: 

        pointer_creator(guessed_letters, letter = guess)
      
      
    print(stages[lives])
    print(blank_word)
    if blank_word.find(guess) != -1 and repeated_guess == True:
      pointer_creator(blank_word, letter = guess)


  #Checking if player won
    if blank_word.count("_") == 0:
      print("You win!")
      gameover = True
      break
    if lives == 0:
      gameover = True
      print("You lose")
      break

    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    
    #Pivitol point where the program pauses
    if len(guess) != 1:
      print("INVALID ENTRY")
    guess = input("Please guess a letter \n")
    if len(guess) == 1:
      valid_entry = True
      guess = guess.lower()
    else:
        valid_entry = False
  if guessed_letters.find(guess) == -1 and blank_word.find(guess) == -1:
    repeated_guess = False
    if chosen_word.find(guess) == -1:
      guessed_letters += guess
      lives -= 1
  else:
    repeated_guess = True
  
  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  letter_in_word = False
  for i in range(word_length):
    if list(chosen_word)[i] == guess:
      blank_list = list(blank_word)
      blank_list[i] = guess
      blank_word = ''.join(blank_list)




