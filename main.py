from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#F3C9D3"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient = "records")
print( to_learn)
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "French", fill = "purple")
    canvas.itemconfig(card_word, text =current_card["French"], fill = "purple")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer = window.after(3000,func= flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Turkish", fill= "white")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill = "white")
    canvas.itemconfig(card_background, image= card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()

window = Tk()
window.title("Flash Card App ")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000,func= flip_card)

canvas = Canvas(width=800, height= 526, bg = BACKGROUND_COLOR, highlightthickness= 0)
card_front_img = PhotoImage(file= "images/card_front.png")
card_back_image= PhotoImage(file= "images/card_back.png")
card_background = canvas.create_image(400,263, image = card_front_img)
card_title = canvas.create_text(400, 150, text= "Title",  font= ("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

cross_image= PhotoImage(file= "images/wrong.png")
unknown_button = Button(image=cross_image, background= BACKGROUND_COLOR, highlightthickness= 1, activebackground= BACKGROUND_COLOR, command= next_card)
unknown_button.grid(row = 1,column= 0)

check_image = PhotoImage(file= "images/right.png")
known_button = Button(image= check_image, background= BACKGROUND_COLOR, highlightthickness= 1, activebackground= BACKGROUND_COLOR, command= is_known)
known_button.grid( row = 1, column = 1)

next_card()
window.mainloop()