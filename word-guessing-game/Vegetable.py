from tkinter import *
from random import *
from tkinter import messagebox
import time

VEGETABLE_WORD = ['MATTOO', 'OTPOAT', 'NGRIEG', 'IRACGL', 'DLAY ENIFRG', 'OLTETGDOBUR', 'UMCPISAC']
VEGETABLE_ANSWER = ['TOMATO', 'POTATO', 'GINGER', 'GARLIC', 'LADY FINGER', 'BOTTLEGOURD', 'CAPSICUM' ]

ran_num = randrange(0, (len(VEGETABLE_WORD)))
jumbled_rand_word = VEGETABLE_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import main_start
        main_start.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(VEGETABLE_WORD)))
        word.configure(text=VEGETABLE_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == VEGETABLE_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score : " + str(points))
            messagebox.showinfo('Correct', "That's Correct! Keep it up!")
            ran_num = randrange(0, (len(VEGETABLE_WORD)))
            word.configure(text=VEGETABLE_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "That's Wrong! Try again!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score : " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=VEGETABLE_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Guess These Vegetables Jumbled Words")
    my_window.configure(background="#e6fff5")
    #my_window.iconbitmap(r'quizee_logo_.ico')
    #img1 = PhotoImage(file="back.png")

    back_btn = Button(
        text="Back",
        width=8,
        borderwidth=2,
        bg='#e6fff5',
        command=back,
    )
    back_btn.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  40 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=check,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()