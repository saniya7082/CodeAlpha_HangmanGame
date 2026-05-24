import random


word_list = ["python", "coding", "player", "matrix", "shadow"]

chosen_word = random.choice(word_list)
word_letters = set(chosen_word)  
guessed_letters = set() 

wrong_guesses = 0
max_guesses = 6

print("--- Welcome to Hangman! ---")
print(f"You have {max_guesses} wrong guesses allowed. Good luck!\n")

while wrong_guesses < max_guesses and len(word_letters) > 0:
 
    display_word = [
        letter if letter in guessed_letters else "_" for letter in chosen_word
    ]
    print("Word to guess: " + " ".join(display_word))
    print(f"Wrong guesses left: {max_guesses - wrong_guesses}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

 
    guess = input("Guess a letter: ").lower().strip()

    
    if len(guess) != 1 or not guess.isalpha():
        print("\n> Invalid input. Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print(f"\n> You already guessed '{guess}'. Try a different letter.\n")
        continue

   
    guessed_letters.add(guess)

    if guess in word_letters:
        print(f"\n> Nice! '{guess}' is in the word.\n")
        word_letters.remove(guess) 
    else:
        print(f"\n> Sorry, '{guess}' is not in the word.\n")
        wrong_guesses += 1

    print("-" * 30)


if len(word_letters) == 0:
    print(f"🎉 Congratulations! You guessed the word: {chosen_word}")
else:
    print(f"💀 Game Over! You ran out of guesses. The word was: {chosen_word}")
