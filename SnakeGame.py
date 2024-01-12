from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE-1) * SPACE_SIZE)
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE - 1) * SPACE_SIZE)

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD_COLOR, tag="food")


def next_turn():
    global direction, score, food

    # move the snake
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    # remove the last coordinate
    last_x, last_y = snake.coordinates.pop()
    canvas.delete(snake.squares[-1])
    snake.squares.pop()

    # create a new square
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
    snake.squares.insert(0, square)

    # check for collisions
    if check_collisions():
        game_over()
        return

    # check if the snake eats the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # increase the score
        score += 1
        label.config(text="Score: {}".format(score))

        # create a new food
        canvas.delete("food")
        food = Food()

        # increase the snake's size
        snake.body_size += 1
        snake.coordinates.append((last_x, last_y))
        square = canvas.create_rectangle(
            last_x, last_y, last_x + SPACE_SIZE, last_y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
        snake.squares.append(square)

    # schedule the next turn
    window.after(SPEED, next_turn)

def change_direction(new_direction):
    global direction

    # prevent the snake from moving in the opposite direction
    if new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
    elif new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction


def check_collisions():
    # get the snake's head coordinates
    x, y = snake.coordinates[0]

    # check if the snake hits the wall
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True

    # check if the snake hits its own body
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    # delete the snake and the food
    canvas.delete("snake")
    canvas.delete("food")

    # display the game over message
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

    # close the window after 3 seconds
    window.after(3000, window.destroy)

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()  # Corrected from winfo_screenmmwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = (screen_height/2)-(window_height/2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

# bind the arrow keys to the change_direction function
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

# start the game
next_turn()

window.mainloop()