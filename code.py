# Write your code here
def main_():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    guessing_word = random.choice(word_list)
    guessed_string = []
    for i in range(len(guessing_word)):  # creation of list(string) containing "-" hypens only, of length equal to the
        guessed_string.append("-")       # length of random word choosen from the list @guessing_word
    n = 0
    word_track_list = []
    while n != 8:
        print()
        print("".join(guessed_string))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not((letter >= 'a') and (letter <= 'z')):
            print("It is not an ASCII lowercase letter")
        elif letter in guessed_string or letter in word_track_list:
            print("You already typed this letter")
        elif letter in guessing_word:
            for i in range(len(guessing_word)):           # changing of all letters if the entered letter matches with the
                if letter == guessing_word[i]:            # letters present in string @guessing_word
                    guessed_string[i] = letter
            if guessing_word == "".join(guessed_string):  # if string matches with the actual random word then break
                break
        else:
            print("No such letter in the word")
            n += 1                                        # attempts reduction
        word_track_list.append(letter)


    if "".join(guessed_string) == guessing_word:
        print("You guessed the word {}!".format("".join(guessed_string)))
        print("You survived!")
    else:
        print("You are hanged!")


import random
print("""
H A N G M A N
""")
status = input('Type "play" to play the game, "exit" to quit:')
while status.lower() == "play":
    main_()
    status = input('Type "play" to play the game, "exit" to quit:')
    
