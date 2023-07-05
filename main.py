#start
import random
from hangman_words import word_list
chosen_word = random.choice(word_list)
print(f"the solution of the choosen word is{chosen_word}")
#generated a random word from hangman_words.py
from hangman_art import logo
print (logo)
word_len = len(chosen_word)
display=[]
print (word_len)
for _ in range(word_len):
    display += "_"
end_game=False
lives=6    
while not end_game:
    guess=input("guess a letter").lower() 
    if guess in display:
        print("you have already entered")
    for position in range(word_len):
        if chosen_word[position]==guess:
            display[position]=guess
    if guess not in chosen_word:
        from hangman_art import stages
        print(stages[lives-1])
        lives-=1
        if lives ==0:
            end_game=True
            print("fool you got failed")
      
    print(f"{''.join(display)}")
    print(chosen_word)
    if "_" not in display:
          end_game=True
          print("you win")          
                


