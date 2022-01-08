"""Yksinkertainen matikkapeli, jossa satunnaisnumeroita 1 ja 9 välillä lisätään yhteen.
   Peli palkitsee kekseillä kun on saanut 5 oikeaa vastausta. Max 4 keksiä ja peli loppuu.
   Susanne Koljonen 29.11.2021"""

from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.title("Math Game!")

# global variables, arvotaan ensimmäiset ruutuun tulevat satunnaiset luvut

randNo1 = random.randint(1, 9)
randNo2 = random.randint(1, 9)
answer = randNo1 + randNo2
win = 0


# functions
def solution():
    solution = entryBox.get()
    entryBox.delete(0, END)
    global answer
    global randNo1
    global randNo2
    global win
    answer = randNo1 + randNo2

    if int(solution) == answer:
        # en löytäny kirveelläkään miten korjata else osion tekstin näkymistä win tekstin alta joten korvataan tyhjillä
        winLabel["text"] = str(solution) + " is correct! Answer is " + str(answer)
        randNo1 = random.randint(1, 9)
        randNo2 = random.randint(1, 9)
        answer = randNo1 + randNo2
        label.config(text=str(randNo1) + " + " + str(randNo2) + " = ")
        win += 1
        label2.config(text="You have " + str(win) + " correct answers!")
    else:
        winLabel["text"] = str(solution) + ", So close!\n The answer was " + str(answer)
        randNo1 = random.randint(1, 9)
        randNo2 = random.randint(1, 9)
        answer = randNo1 + randNo2
        label.config(text=str(randNo1) + " + " + str(randNo2) + " = ")
    # tarkistetaan voittopisteitä, jos pisteitä on yli 5, 10, 15, 20, saa keksin.
    if win == 5:
        winLabel["text"] = "Have a cookie!"
        cookieLabel = Label(frame, image=cookie)
        cookieLabel.grid(row=4, column=0)
    if win == 10:
        winLabel["text"] = "Have another cookie!"
        cookieLabel = Label(frame, image=cookie)
        cookieLabel.grid(row=4, column=1)
    if win == 15:
        winLabel["text"] = "Have another cookie!"
        cookieLabel = Label(frame, image=cookie)
        cookieLabel.grid(row=4, column=2)
    if win == 20:
        global button1
        global button2
        winLabel["text"] = "You have all the cookies!"
        cookieLabel = Label(frame, image=cookie)
        cookieLabel.grid(row=4, column=3)
        # disabloidaan napit, peli on päättynyt
        button1["state"] = DISABLED
        button2["state"] = DISABLED

# käyttäjä voi halutessaan pyytää uudet numerot jos ei osaa ratkaista annettua tehtävää
def renew():
    global randNo1
    global randNo2
    global answer
    randNo1 = random.randint(1, 9)
    randNo2 = random.randint(1, 9)
    answer = randNo1 + randNo2
    label.config(text=str(randNo1) + " + " + str(randNo2) + " = ")


# frames
frame = LabelFrame(root, text="Solve the problem", padx=50, pady=50)

# labels
label = Label(frame, text=str(randNo1) + " + " + str(randNo2) + " = ")
label2 = Label(frame, text="You have " + str(win) + " correct answers!")
winLabel = Label(frame, text="")

# entry
entryBox = Entry(frame, width=5)

# images
cookie = ImageTk.PhotoImage(Image.open("cookie.png"))

# button
button1 = Button(frame, text="Pass", padx=20, command=renew)
button2 = Button(frame, text="Enter", padx=20, command=solution)

# shove stuff in
frame.pack(padx=10, pady=10)
label.grid(row=0, column=0, pady=20, columnspan=2)
entryBox.grid(row=0, column=2, pady=10, columnspan=2)
button1.grid(row=1, column=0, columnspan=2)
button2.grid(row=1, column=2, columnspan=2)
winLabel.grid(row=2, columnspan=3)
label2.grid(row=3, columnspan=3)

# main loop
root.mainloop()
