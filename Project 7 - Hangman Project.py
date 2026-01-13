import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Words to guess: {display}")

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"****************************{lives} LIVES LEFT****************************\n"
          f"{hangman_art.stages[lives]}")

    guessed_letters.append(guess)

    if lives == 0:
        game_over = True
        print((f"***********************YOU Lose**********************\n"
              f"The word you were trying to guess was {chosen_word}"))
    if "_" not in display:
        game_over = True
        print("***********************CONGRATULATIONS YOU Win!**********************")
