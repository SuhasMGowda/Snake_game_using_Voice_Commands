# Snake Game with Voice Commands

This project is a simple yet engaging implementation of the classic Snake game, but with a twist! Instead of using the keyboard, you control the snake using voice commands. The game is built using Python and Tkinter for the graphical user interface, with the `speech_recognition` library for handling voice inputs.

## Features

- **Voice-Controlled Movement:** Use voice commands like "up," "down," "left," and "right" to control the snake.
- **Snake Growth:** The snake grows in length every time it eats the food.
- **Boundary Wrapping:** The snake reappears on the opposite side of the screen when it crosses the boundaries.
- **Pause and Resume:** You can pause and resume the game using buttons on the interface.
- **User-Friendly Interface:** Clear buttons and messages guide the user through starting, pausing, and resuming the game.
- **Keyboard Control Option:** A version of the game with keyboard arrow controls is also included for comparison.

## Technologies Used

- **Python 3.12:** The programming language used to develop the game.
- **Tkinter:** Used to create the graphical user interface.
- **SpeechRecognition:** Python library used to handle voice command inputs.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/snake-game-voice-control.git
   cd snake-game-voice-control
   ```

2. **Install the required Python packages:**

   ```bash
   pip install tkinter speechrecognition pyaudio
   ```

3. **Run the game:**

   ```bash
   python snake_game_voice.py
   ```

## How to Play

1. **Start the Game:**
   - Click the "Start" button to begin the game.
   - The game will wait for your voice command to move the snake.

2. **Control the Snake:**
   - Speak commands like "up," "down," "left," or "right" to move the snake in the desired direction.

3. **Eat Food:**
   - The goal is to guide the snake to eat the red food squares. The snake will grow longer each time it eats.

4. **Pause/Resume:**
   - You can pause the game by clicking the "Pause" button and resume by clicking "Play."

5. **Boundary Wrapping:**
   - If the snake crosses the screen edge, it will reappear from the opposite side.

6. **Game Over:**
   - The game ends if the snake runs into itself. You can restart by clicking "Start."

## Known Issues

- **Speech Recognition Delay:** The game may experience slight delays in processing voice commands. Make sure your microphone is functioning well and that you speak clearly.
- **Microphone Access:** Ensure that your microphone is accessible to the application. Some systems may require permission to use the microphone.

## Future Improvements

- Adding more complex commands for advanced gameplay.
- Implementing difficulty levels that increase the speed of the snake as it grows.
- Adding background music and sound effects for a more immersive experience.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions, bug reports, and feature suggestions are always welcome!
