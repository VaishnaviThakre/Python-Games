from tkinter import *

def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            import Animals
            Animals.main()
        elif args == 2:
            import Body_parts
            Body_parts.main()
        elif args == 3:
            import Colour
            Colour.main()
        elif args == 4:
            import Fruit
            Fruit.main()
        elif args == 5:
            import Shapes
            Shapes.main()
        elif args == 6:
            import Vegetable
            Vegetable.main()
        elif args == 7:
            import Vehicles
            Vehicles.main()

    def option():

        sel_btn1 = Button(
            text="Animals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Body parts",
            width=18,
            borderwidth=8,
            font=("",18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Colour",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Fruits",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Shapes",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Vegetable",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        sel_btn7 = Button(
            text="Vehicles",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="black",
            bg="skyblue",
            cursor="hand2",
            command=lambda: start_game(7),
        )
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
        sel_btn7.grid(row=6, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()
        #lab_img.destroy()
        option()

    main_window = Tk()
    main_window.geometry("380x500")
    main_window.resizable(0, 0)
    main_window.title("!!! GUESS THE WORD !!!")
    main_window.configure(background="yellow")

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="white",
        bg="red",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.place(x=95,y=180)

    main_window.mainloop()


start_main_page()