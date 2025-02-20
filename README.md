# Rock-Paper-Scissors-game

## Description
This is a computer vision-based Rock Paper Scissors game that allows a player to compete against an AI. The game utilizes OpenCV for real-time hand tracking and gesture recognition, enabling players to make moves using hand signs.

## Features
- Real-time hand tracking using OpenCV and cvzone.
- AI-generated moves for fair gameplay.
- Score tracking for both AI and Player.
- Interactive graphical interface.

## How It Works
1. The game starts when the user presses 's'.
2. A 3-second countdown is displayed.
3. The player's hand gesture is recognized and compared against a randomly generated AI move.
4. The winner is determined based on the standard Rock Paper Scissors rules:
   - Rock (Fist) beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
5. The score is updated accordingly.
6. The game continues until manually stopped.

## Requirements
Ensure you have the following dependencies installed:
- Python 3.x
- OpenCV (`cv2`)
- cvzone
- NumPy

## Installation and Requirements

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Rock-Paper-Scissors-game.git
   cd Rock-Paper-Scissors-game
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python cvzone numpy
   ```
3. Place the required image assets inside an Images/ folder:
```
Images/
├── Background.png
├── 1.png  # Rock
├── 2.png  # Paper
├── 3.png  # Scissors
```
