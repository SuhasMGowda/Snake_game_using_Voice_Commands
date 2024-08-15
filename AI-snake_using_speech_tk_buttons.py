import tkinter as tk
import random
import speech_recognition as sr

# Initialize the main window
root = tk.Tk()
root.title("Voice-Controlled Snake Game")
root.resizable(False, False)

# Set the game dimensions
width = 400
height = 400
cell_size = 20

# Create a canvas for the game
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

# Add a label to display messages
message_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="black")
message_label.pack()

# Initial snake position and food position
snake = [(width // 2, height // 2)]
snake_dir = "stop"
food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
        random.randint(0, (height - cell_size) // cell_size) * cell_size)

# Variables to control the game state
game_running = False
paused = False

# Function to draw the snake and food
def draw_snake_and_food():
    canvas.delete("all")
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + cell_size, segment[1] + cell_size, fill="green")
    canvas.create_rectangle(food[0], food[1], food[0] + cell_size, food[1] + cell_size, fill="red")

# Function to move the snake
def move_snake():
    global snake, food, snake_dir, game_running, paused

    if game_running and not paused and snake_dir != "stop":
        x, y = snake[0]

        if snake_dir == "up":
            y -= cell_size
        elif snake_dir == "down":
            y += cell_size
        elif snake_dir == "left":
            x -= cell_size
        elif snake_dir == "right":
            x += cell_size

        # Wrapping logic
        if x < 0:
            x = width - cell_size
        elif x >= width:
            x = 0
        if y < 0:
            y = height - cell_size
        elif y >= height:
            y = 0

        new_head = (x, y)
        snake = [new_head] + snake[:-1]

        # Check if snake eats food
        if snake[0] == food:
            snake.append(snake[-1])  # Grow snake
            food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
                    random.randint(0, (height - cell_size) // cell_size) * cell_size)

        # Check for collisions with itself
        if len(snake) != len(set(snake)):
            game_over()
            return

    draw_snake_and_food()
    root.after(50, move_snake)  # Reduced delay for faster game loop

# Function to end the game
def game_over():
    global snake_dir, game_running
    snake_dir = "stop"
    game_running = False
    message_label.config(text="Game Over! Press Start to play again", fg="red")

# Function to restart the game
def restart_game():
    global snake, snake_dir, food, game_running, paused
    snake = [(width // 2, height // 2)]
    snake_dir = "stop"
    food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
            random.randint(0, (height - cell_size) // cell_size) * cell_size)
    game_running = True
    paused = False
    message_label.config(text="")
    move_snake()

# Function to update the snake direction based on voice commands
def update_direction(recognizer, audio):
    global snake_dir
    try:
        command = recognizer.recognize_google(audio).lower()
        message_label.config(text=f"Command received: {command}", fg="white")

        if command == "up" and snake_dir != "down":
            snake_dir = "up"
        elif command == "down" and snake_dir != "up":
            snake_dir = "down"
        elif command == "left" and snake_dir != "right":
            snake_dir = "left"
        elif command == "right" and snake_dir != "left":
            snake_dir = "right"
        elif command == "pause":
            pause_game()
        elif command == "play":
            resume_game()
    except sr.UnknownValueError:
        message_label.config(text="Sorry, I didn't catch that.", fg="orange")
    except sr.RequestError as e:
        message_label.config(text=f"Error: {e}", fg="red")

# Initialize the recognizer and microphone
recognizer = sr.Recognizer()

# Adjust for ambient noise in a separate context
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.1)  # Reduced ambient noise adjustment time

# Start continuous listening in the background
microphone = sr.Microphone()
stop_listening = recognizer.listen_in_background(microphone, update_direction)

# Function to pause the game
def pause_game():
    global paused
    paused = True
    message_label.config(text="Game Paused. Say 'Play' or press Play button to resume.", fg="yellow")

# Function to resume the game
def resume_game():
    global paused
    paused = False
    message_label.config(text="Game Resumed", fg="white")

# Function to create the start screen
def start_screen():
    start_button = tk.Button(root, text="Start", font=("Arial", 14), command=restart_game)
    start_button.pack(pady=10)

    pause_button = tk.Button(root, text="Pause", font=("Arial", 14), command=pause_game)
    pause_button.pack(pady=5)

    play_button = tk.Button(root, text="Play", font=("Arial", 14), command=resume_game)
    play_button.pack(pady=5)

# Initialize the game
start_screen()

# Run the tkinter main loop
root.mainloop()
