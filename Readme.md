# Tetris Game

A classic implementation of the Tetris game, built in python input rendered by a lexicographic analyser  for educational purposes. This project demonstrates the fundamental concepts of game development, including game loop, input handling, rendering, and tetromino generation and movement.

## Features

- **Customizable Game Settings**: Configure the game window dimensions, update rate, and falling speed to tailor the gameplay experience.
- **Colorful Rendering**: Choose from different color schemes for the background and tetrominoes for a visually appealing game.
- **Score Tracking**: Keep track of your score as you clear lines and progress through the game.
- **Smooth Gameplay**: Enjoy a seamless gaming experience with efficient rendering and precise tetromino movements.
- **Intuitive Controls**: Use the arrow keys to move and rotate the tetrominoes, making the gameplay easy to pick up.

## Prerequisites

Before building and running the Tetris game, ensure that you have the following tools installed:

- `gcc` (GNU Compiler Collection)
- `make` (GNU Make)
- `clang-format` (for automatic code formatting)
- `numpy` (pip install numpy)
- `tkinter` (sudo apt-get install python3-tk)

## Getting Started

Follow these steps to build and run the Tetris game:

1. Build the game: (Run the given command in the terminal)
"make build"

2. Run the game:
"make test && python3 output.py" 

This will run the tetris game according to the predefined input given in `testinput.tetris` by the game programmer/ player.

The python code generated after the Syntax Directed Translation(SDT) can be viewed in translated.py

-------------------------------------------------------------------------------------------------------------------------------------------------------------
# VERY IMPORTANT NOTE: In order to successfully play the game, you(the game programmer/ player) MUST specify these(given below) variables in Section1 of the input file.
-------------------------------------------------------------------------------------------------------------------------------------------------------------

- `height`: Height of the game window (default: 20)
- `width`: Width of the game window (default: 10)
- `update_duration`: Duration between game updates in milliseconds (default: 100)
- `difficulty`: Difficulty in levels ranging from 0-9
- `background_col`: Background color (refer to the color index)
- `foreground_col`: Tetromino color  (refer to the color index)
- `rotation_limit`: The total number of rotations allowed (default being infinity)

The available color options are:

| Option | Color            |
|--------|------------------|
| 0      | Light Gray       |
| 1      | Blue             |
| 2      | Red              |
| 3      | Green            |
| 4      | Yellow           |
| 5      | Orange           |
| 6      | Black            |

-------------------------------------------------------------------------------------------------------------------------------------------------------------
## INPUT FORMAT
  - You have to give the input in the tetrisinput.tetris in the same format as mentioned earlier
  - Pass in the different parameters build and run the code to play with the tetris
-------------------------------------------------------------------------------------------------------------------------------------------------------------
## Features Provided
### 1. Score

- **Description**: Keeps track of the player's score as they clear lines.
- **Usage**: The score increases each time the player clears a line.

### 2. Pause

- **Description**: Allows the player to pause and resume the game.
- **Usage**: Press the "Pause" button in the game menu to pause the game. Press again to resume.

### 3. New Game

- **Description**: Starts a new game.
- **Usage**: Select "New Game" from the game menu to start a new game.

### 4. Exit

- **Description**: Exits the game.
- **Usage**: Select "Exit" from the game menu to exit the game.

### 5. Speedup/Speed_Down

- **Description**: Speeds up/Speed Down the tetris pieces.
- **Usage**: Select "Speedup/SpeedDown" from the game menu to exit the game.

### 6. Save state

- **Description**: Save the current state.
- **Usage**: Saves the current state of the game in the desired location




## How to Use

1. Clone the repository or download the Tetris Engine files.
2. Run the game.
3. Use the arrow keys to move and rotate Tetriminos.
4. Press the space bar to drop Tetriminos faster.
5. Navigate the game menu using the arrow keys and press Enter to select an option.
6. Play the game and enjoy!
-------------------------------------------------------------------------------------------------------------------------------------------------------------
****
