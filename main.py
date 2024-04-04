#Step 1 


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."



import random
import list_of_words
import acsi_day7
import os 

os.system('cls') 

print(acsi_day7.logo)
chosen_word = random.choice(list_of_words.words)
# print(f'{chosen_word} \n')

display = []

for i in chosen_word:
    display.append('_')

display_words = ''
for i in display:
    display_words += i + ' '
print(display_words)

lives = 6

while '_' in display and lives > 0: 

    guess = (input('\nGuess the letter ! ')).lower() 

    os.system('cls')   

    if guess in display:
        print('You already chose this word, try again ...')
        continue

    n = 0
    for i in chosen_word:    
        if guess == i : 
            display[n] = i 
        n += 1    
    
    display_words = ''
    for i in display:
        display_words += i + ' '
    print(f'\n{display_words}')
    

    if guess not in display:
        lives -= 1
        print(f'\nYou guess a letter {guess}, thats not in the word. You lose a life.')
        print(acsi_day7.stages[lives])
        print(f'\nYou have {lives} lives.')
    else: 
        print(f'\nYou guess a letter {guess}')
        print(acsi_day7.stages[lives])
        print(f'\nYou have {lives} lives.')

if lives <= 0: 
    print(f'\nYou lose \nThe word was {chosen_word}')
else: 
    print('\nYou win the game !!!')