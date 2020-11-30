#***** Guess My Number Game Tkinter Version IS125 Cory Friedt *****#

# IMPORT LIBRARIES, SET ATTEMPTS & RANDOM NUMBER

from tkinter import *
import random

attempts = 10

random_number = random.randint(1,100)

# GAME LOGIC

def check():
    global attempts
    global text

    attempts -= 1  # decrement attempts by 1

    guess = int(entry_window.get())  # store user's guss in a variable

    entry_window.delete(0, END)  # clear input field

    if random_number == guess:  # correct answer case
        text.set("You win!")
        btn_check.pack_forget()
    elif attempts == 0:  # out of attempts case
        text.set("You are out of attempts!")
        btn_check.pack_forget()
    elif guess < random_number:  # lower than case
        text.set("Incorrect! You have " + str(attempts) + " remaining - The answer is higher!")
    elif guess > random_number:  # greater than case
        text.set("Incorrect! You have " + str(attempts) + " remaining - The answer is lower!")            

root = Tk()  # set variable for window

root.title("Guess My Number Game Tkinter Version")  # set window title

root.geometry("500x200")  # set window size

label = Label(root, text="Guess a number between 1 & 100")  # create instruction label
label.pack()

entry_window = Entry(root, width=40, borderwidth=4)  # create entry window
entry_window.pack()

btn_check = Button(root, text="Check", command=check, bg="red", fg="white")  # create button to confirm guess
btn_check.pack()

btn_quit = Button(root, text="quit", command=root.destroy)  # create a quit button
btn_quit.pack()

text = StringVar()  # display number of attempts to user
text.set("You have 10 attempts remaining!")

guess_attempts = Label(root, textvariable=text)  # update text
guess_attempts.pack()



root.mainloop()  # run tkinter