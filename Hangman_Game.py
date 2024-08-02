#Hangman Game : Guess word to save your partner life.

import random,time,sys
from AsciiArt import start,gameover,getStageAsciiArt,getSaveAsciiArt #AsciiArt in AsciiArt.py
import requests #for getting words using http request

print(start) #Show AsciiArt

print("Hangman Game by @tusharharyana")
time.sleep(2)
print("Before starting game please answer the questions correctly for more fun!")
time.sleep(2)
name = input("What's your name dear : ")
name = name.capitalize()

stages = getStageAsciiArt(name)
save = getSaveAsciiArt(name)

time.sleep(1)
status = input(f"Hi {name}, Are you Single ? (Y/N) : ")


if status == 'Y' or status == 'y':
    time.sleep(2)
    print(f"I get it {name}, don't worry—you'll find someone special soon.")
    time.sleep(4)
    print(f"{name} Your dedication to your future Girlfriend will be tested. Guess well if you care, or let the Hangman have his fun!")
elif status == 'N' or status == 'n':
    time.sleep(2)
    print(f"So nice! {name} Even if it seems like no one loves you right now, it's all good—let's play!")
    time.sleep(4)
    print(f"{name} Your dedication to your Wife OR Girlfriend will be tested here. Guess well if you care, or let the Hangman have his fun!")
else:
    print("Enter Y or N not other keys :)")
    sys.exit()

#Random word chooser
#word_list = ['Mirzapur','Gadar','Love','GirlFriend','Baby']

#Fetch random word list from Datamuse.com
def fetch_words():
    url =  "https://api.datamuse.com/words?rel_jja=animal"
    response = requests.get(url)
    data = response.json()
    if data:
        return [word['word'] for word in data]
    return []


# Main game logic
word_list = fetch_words()    
if word_list:  
   random_word = random.choice(word_list).lower()
#    print(random_word)
else:
    print("No movies")
    sys.exit()
    
    
#Initialize the game
def initialize_game(random_word, reveal_count=2):
    word_length = len(random_word)
    word_spaces = [" _ " for _ in range(word_length)]
    
    # Reveal a few letters at the start
    positions = random.sample(range(word_length), min(reveal_count, word_length))
    for pos in positions:
        word_spaces[pos] = random_word[pos]
    
    return word_spaces

#Create a word list having some letters. ex:['R','a','_','_','e']
word_spaces = initialize_game(random_word)
print("\t")
print(' '.join(word_spaces)) #Convert list to string #R a _ _ e
print("\n")

#Player will have 6 chances to guess word.
lives = 6
 
#Logic to start Guess   
while True:
   guess = input('Guess a letter: ').lower()
   if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
   if guess in random_word:
        for position in range(len(random_word)):
            if random_word[position] == guess:
                word_spaces[position] = guess
        print(' '.join(word_spaces))
   else:            
        lives -=1
        if lives == 0:
            print(f"Word is : {random_word}")
            print(stages[lives])
            break     
        print(stages[lives])
    
        
   if " _ " not in word_spaces:
        print(f"Word is : {random_word}")
        print(gameover)
        print(save)
        break     
    
        
