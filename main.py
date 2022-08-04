import re
import string

print("""
Welcome to the 'Wordle' helper program! This was created to help
you keep your 'Wordle' streak if you get stuck on word.

Please press enter to continue""")
input()
print("""
Don't know what 'Wordle' is? Type 'summary' to learn the rules,
otherwise hit enter to continue.""")

while True:
    summary = input().lower().strip()
    if summary == 'summary': # Provide optional summary of the game.
        print("""For today's Wordle and full rules, please see this webpage:
        https://www.nytimes.com/games/wordle/index.html .

        A basic summary is that you have six tries to guess a mystery five-letter
        word. If you guess the right letter in the right spot, that square turns green
        which gives you a good clue to word. If you guess the right word in the wrong
        spot, that square turns yellow, which gives you a clue to the word as well. If
        the word you guess has letters that are not in word, those letters will turns
        grey or black. This program will help you guess the word if you're stuck based on
        what you already have tried.

        Ready to try it? Hit enter to continue
        """)
        break
    elif summary == '':
        break
    else:
        print("Please hit enter or type 'summary'")
        continue

print("""\nBelow, you'll have a chance to enter the letters you know for sure (green
letters), the letters you know are in the word but unsure of the order (yellow letters)
and the letters you know ARE NOT in the word (the black/grey letters).\n
Are you ready to continue? Press 'Enter' to continue type 'quit' to quit. """)

cont = input('').lower().strip()
if cont == 'quit':
    quit()

print("""Great! Let's get started. First we will ask you for the
the green letters. If the letter is not green on your board, just
hit enter to pass to the next letter.\n""")


known=[] # Take input from user, check for errors.
order = ['first', 'second', 'third', 'fourth', 'fifth']
for each in range(5):
    k_let = (input(f"If you know it, enter the {order[each]} letter or press enter to skip: ").lower()).strip()
    if not k_let.isalpha() and k_let != '':
        print("Letters only or 'enter' only! Please try again.")
        quit()
    elif len(k_let) > 1:
        print("We're asking for one letter at time, please try again!")
        quit()
    else:
        known.append(k_let)


def pattern_create(known_numbers: list)-> str:
    """Create a ReGex pattern from the User Input of known numbers."""
    for letters in range(5):
        if known[letters] == '':
            known[letters] = '.'
    return ''.join(known)


fhand = open('5_letter_words.txt') # Text document contains all 5-letter words
matches_pattern = [word.strip() for word in fhand if re.match(pattern_create(known), word)] # Keep the ones that match the known pattern.

print("""Thanks for inputing your known letters. Let's move on to the yellow letters.
Please enter all the letters on a single line.\n""")
glet = input("Please list the yellow letters, those you know are in the word but you don't know which letter:\n ").lower().strip()
good_letters = list(glet.translate(str.maketrans('', '', string.punctuation)))
if any(char.isdigit() for char in good_letters):
    print("Numbers aren't allowed. Please try again.")
    quit()
print("""\nThanks for inputing your yellow letters. Let's move on to the grey/black letters.
Please enter all the letters on a single line. These are letters you know are not
in the word.\n""")
blet = input("Please list the grey or black letters, those you know are NOT in the word: ").lower().strip()
bad_letters = list(blet.translate(str.maketrans('', '', string.punctuation)))
if any(char.isdigit() for char in bad_letters):
    print("Numbers aren't allowed. Please try again.")
    quit()

def exclude_characters(pattern_list: list, good_list: list, bad_list: list)-> list:
    """Takes the words that fit the pattern so far and confirms they contain all letters from the good_list and none from the bad list.
    Returns a list of words to exclude."""
    excluded = []
    for word in pattern_list:
        for letter in bad_list:
            if letter in word:
                excluded.append(word)
        for letter in good_list:
            if not letter in word:
                excluded.append(word)
    return excluded

new = sorted(set(matches_pattern).difference(set(exclude_characters(matches_pattern, good_letters, bad_letters))))
plural = 's' if len(new)> 1 else ''
if not new:
    print("No known English words match those parameters.")
else:
    print(f"Your have {len(new)} option{plural}: ")
    for each in new:
        print(each, end=' ')
