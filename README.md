# wordle-helper
My first ever original program: a program to help you cheat on NYT's 'Wordle' game.

[Don't know what Wordle is? You should. Click here!](https://www.nytimes.com/games/wordle/index.html)

After learning regular expressions in python I had the idea to create this program to help me cheat... uhh.. I mean 'improve'... on Wordle.

There is a lot of room for improvement and will likely come back to this as I get better to make a prettier interface and more concise code/efficient code. 

I struggled with consolidating the loops for checking againsts multiple lists (the pattern-matched words plus the lists of included and excluded letters) and with being able to let the user start-over if they accidently selected an invalid number.

***update*** 8/6/2022: I took what little Tkinter I learned while doing the MineSweeper Guided Project and applied it to create a basic GUI this program. It has some limitations: mainly the ability to restart instead of quit. I'm still looking for a solution!

Also, my initial button function does not follow the DOT prinicple and I need to consider how to break it down into simpler functions that do one thing. 

***update*** 8/9 : learned a few more Tkinter things. Unfortuntaely the program doesn't look the same at all on replit as the buttons are messed up(overlapping) and for some reason it doesn't recognize the image module PIL. Updated a slightly amended less quality version.

I accomplished a few things in this rendition:
1) Intead of quit I discovered how to clear the entries and labels (and then I didn't need quit or reset).
2) Instead of dealing with overlapping labels, I figured out how to change (configure) the same label. 
3) Made the buttons more organized/centered althought they don't look as good on replit.
4) Added an image to it, (doesn't work in the replit version).

[version 3,fixed a few bugs]([https://replit.com/@zambonibecky/WordleHelperV3?embed=1])

[I uploaded version 2 with GUI here.](https://replit.com/@zambonibecky/WordleHelperV2?v=1)

I hope to update again soon as I learn more!

[This is the first version with no GUI.](https://replit.com/@zambonibecky/WordleHelper?v=1)
