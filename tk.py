from tkinter import *
import re
import webbrowser


root = Tk()
root.geometry('250x400')
root.title("Wordle Helper")

label1 = Label(root, text = 'Wordle Helper', font=("Arial", 20)).grid(row=0, column = 0, columnspan=10)

entry1 = Entry(root, width = 3, bg = 'green', font='bold')
entry1.grid(row=2, column =0)
entry2 = Entry(root, width =3, bg = 'green', font='bold')
entry2.grid(row=2,column=1)
entry3 = Entry(root, width = 3, bg = 'green', font='bold')
entry3.grid(row=2, column =2)
entry4 = Entry(root, width =3, bg = 'green', font='bold')
entry4.grid(row=2,column=3)
entry5 = Entry(root, width =3, bg = 'green', font='bold')
entry5.grid(row=2,column=4)

label2 = Label(root, text = "Enter known green letters above.\nLeave blank if none.").grid(row=3, column = 0, columnspan=5)

g_letters = Entry(root, width = 20, bg = 'yellow', font='bold')
g_letters.grid(row=4, column =0, columnspan = 5, padx=10)

label3 = Label(root, text = "Enter all yellow letters above.\nLeave blank if none.").grid(row=5, column = 0, columnspan=5)

b_letters = Entry(root, width = 20, bg = 'gray', font='bold')
b_letters.grid(row=6, column =0, columnspan = 5)

label4 = Label(root, text = "Enter gray/black letters above.").grid(row=7, column = 0, columnspan=5)


def button_command(): #limitation: thisis a huge function not abiding by DOT principal. How to break up..?
    """Get and validate user all inputs."""
    known = validate([entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get()])
    good_letters = validate(list(g_letters.get()))
    bad_letters = validate(list(b_letters.get()))
    regex = get_reg(known)
    fhand = open('5_letter_words.txt') # Text document contains all 5-letter words
    matches_pattern = [word.strip() for word in fhand if re.match(regex, word)] # Keep the ones that match the known pattern.
    if not matches_pattern:
        label5 = Label(root, text = "No known English words match\nthose parameters.", fg = 'red').grid(row=8, column = 0, columnspan=5, rowspan = 2)
        raise ValueError("No words found.")
    new = sorted(set(matches_pattern).difference(set(exclude_characters(matches_pattern, good_letters, bad_letters))))
    plural = 's' if len(new)> 1 else ''
    label6 = Label(root, text = f"You have {len(new)} option{plural}:", fg = 'green').grid(row=8, column = 0, columnspan=5)
    def show():
        label7 = Label(root, text = ', '.join(new), wraplength = 200).grid(row=10, column = 0, columnspan=10)
    entry1.delete(0, 'end'), entry2.delete(0, 'end'), entry3.delete(0, 'end'), entry4.delete(0, 'end'), entry5.delete(0, 'end'), g_letters.delete(0, 'end'), b_letters.delete(0, 'end')
    enter = Button(root, text='See words', command = show)
    enter.grid(row=9, column =0, columnspan=5)


def validate(list):
    """Raises error if invalid characters entered. Replaces uppercase letters.""" #limitation: commas
    index = 0
    for each in list:
        if len(each) > 1:
            label8 = Label(root, text = "Only one letter\nper green box.", fg = 'red').grid(row=8, column = 0, columnspan=5, rowspan = 2)
            raise ValueError("Only letters or blanks allowed.")
        if each.isalpha() or each == '' or each == ',':
            if each.isupper():
                list[index] = each.lower()
            index += 1
            continue
        else:
            label9 = Label(root, text = "Only letters or blank\nspaces are permitted.", fg = 'red').grid(row=8, column = 0, columnspan=5, rowspan = 2)
            raise ValueError("Only letters or blanks allowed.")
    return list


def get_reg(list: [str])-> str:
    """Get the regex for the green letters."""
    for letters in range(5):
        if list[letters] == '':
            list[letters] = '.'
    return ''.join(list)


def exclude_characters(pattern_list: list, good_list: list, bad_list: list)-> list:
    """Take the words that fit the pattern so far and confirm words contain all letters from the good_list and none from the bad list.
    Return a list of words to exclude."""
    excluded = []
    for word in pattern_list:
        for letter in bad_list:
            if letter in word:
                excluded.append(word)
        for letter in good_list:
            if not letter in word:
                excluded.append(word)
    return excluded


def callback(url):
    """Click link to NYT description."""
    webbrowser.open_new_tab(url)


def leave():
    """User quit.""" # limitation: restart
    quit()


submit = Button(root, text='Submit', command = button_command)
submit.grid(row=9, column =0, columnspan=5)

restart = Button(root, text='Quit', command = leave)
restart.grid(row=13, column =0, columnspan=5)

link = Label(root, text="What's 'Wordle'?", fg="blue", cursor="hand2")
link.grid(row=1, columnspan=5)
link.bind("<Button-1>", lambda e: callback("https://www.nytimes.com/games/wordle/index.html"))

root.mainloop()
