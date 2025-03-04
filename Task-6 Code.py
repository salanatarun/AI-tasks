print("Hangman Game")
import random
import nltk
from nltk.corpus import words

# Download the word dataset if not already downloaded
nltk.download("words")

# Load a dictionary of words
WORD_LIST = set(words.words())

# Get words of a specific length
def get_valid_words(length):
    return [word.lower() for word in WORD_LIST if len(word) == length]

# Calculate letter frequency in English words
def get_letter_frequencies():
    letter_counts = {}
    for word in WORD_LIST:
        for letter in word.lower():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return sorted(letter_counts, key=letter_counts.get, reverse=True)

# AI-based letter guessing strategy
def guess_letter(remaining_letters, used_letters):
    for letter in remaining_letters:
        if letter not in used_letters:
            return letter
    return None  # No letters left to guess

# Hangman game implementation
def hangman_ai():
    print("Welcome to AI Hangman!")

    word_length = int(input("Player 1: Enter the word length: "))
    valid_words = get_valid_words(word_length)

    if not valid_words:
        print("No words found for this length. Try a different length.")
        return

    secret_word = random.choice(valid_words)  # AI chooses a secret word
    guessed_word = ["_"] * word_length
    incorrect_guesses = 0
    max_attempts = 6  # Hangman typically allows 6 incorrect guesses

    used_letters = set()
    letter_frequencies = get_letter_frequencies()

    print("\nPlayer 2: Start guessing!\n")

    while incorrect_guesses < max_attempts and "_" in guessed_word:
        print("Current word: ", " ".join(guessed_word))
        print("Incorrect guesses: ", incorrect_guesses)

        guessed_letter = guess_letter(letter_frequencies, used_letters)
        if guessed_letter is None:
            break

        print(f"AI guesses: {guessed_letter}")
        used_letters.add(guessed_letter)

        if guessed_letter in secret_word:
            for idx, char in enumerate(secret_word):
                if char == guessed_letter:
                    guessed_word[idx] = guessed_letter
        else:
            incorrect_guesses += 1

        if "_" not in guessed_word:
            print("\nPlayer 2 wins! The word was:", secret_word)
            return

    print("\nPlayer 1 wins! The word was:", secret_word)

# Run the game
if __name__ == "__main__":
    hangman_ai()
