import random
from word import words
import string
import ast


def get_valid_word(words):
    valid_word = random.choice(words)
    while "-" in words or " " in words:
        valid_word = random.choice(words)
        valid_word = valid_word.upper()
    return valid_word

def hangman():
    word = get_valid_word(words)
    print("")
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    random_num =random.randint(1,len(word)//2)
    # for randomly un reveling half of the letters of the word
    # str object has no attribute remove error
    # while random_num:
    #     random_index = random.randint(1,len(word))
    #     letter = word[random_index]
    #     used_letters.add(letter)
    #     word.remove(letter)
    #     random_num=random_num-1
    while len(word)>0 and lives>0:
       print("you have ",lives," lives and you used following letters ",(" ").join(used_letters))
       word_list = [letter if letter in used_letters else '-' for letter in word]
       print("\n",(" ").join(word_list))
       user_input = input("guess a letter:").upper()
       if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word:
                word.remove(user_input)
            else:
                lives = lives - 1
                print("your guess is wrong")
       elif user_input in used_letters:
            print("oops you used that letter before")
       else:
            print("Invalid character try again")
    if lives == 0:
        print("sorry your lives over\n")
        print("the correct word is",word)
    else:
        print("hurry you guessed correctly")

hangman()        