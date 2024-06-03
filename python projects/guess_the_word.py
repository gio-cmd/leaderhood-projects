import random

# list of words to guess in the game
words = ["tree", "banana", "waterfall", "alucha", "omlet", "house", "castle"]

#select a random word
def choose_word(words):
    return random.choice(words)

# this shows how many letters we have guessed alredy
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    word = choose_word(words)
    guessed_letters = set()
    attempts = 6
    guessed_word = False

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(word)} letters.")
    
    # game loop
    while attempts > 0 and not guessed_word:
        # what letters are guessed displayed with func
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        
        # player guess
        guess = input("Guess a letter or the whole word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            # check if the letter has already been guessed
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.add(guess)
                print("Good guess!")
                # check if all letters in the word have been guessed
                if set(word).issubset(guessed_letters):
                    guessed_word = True
            else:
                guessed_letters.add(guess)
                attempts -= 1
                print("Incorrect guess.")
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed_word = True
                guessed_letters.update(word)
            else:
                attempts -= 1
                print("Incorrect guess.")
        else:
            print("Invalid input. Please guess a single letter or the entire word.")
        
        print()
    
    if guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    # if the player ran out of attempts
    else:
        print(f"Game Over! The word was: {word}")

play_game()

