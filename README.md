# Tamagotchi Hamster 🐹

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python version" />

A virtual pet simulation game where you take care of a hamster. Keep your hamster alive by feeding and playing with it!

## Features
- Real-time hamster state tracking
- Life and play level indicators
- Interactive feeding and playing
- State changes based on hamster's condition
- Persistent game state saving
- Background music

## Installation
1. Clone the repository
```bash
git clone https://github.com/NikitaTurbo/tamagotchi.git
cd tamagotchi
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## How to Play
1. Run the game:
```bash
python main.py
```

2. Use the interface to:
   - Monitor hamster's life and play levels
   - Feed the hamster to restore its life
   - Play with the hamster to keep it happy

3. Keep your hamster alive by maintaining its life and play levels above 0

## Game Mechanics
- Life decreases by 1 point every second
- Play decreases by 1 point every 10 seconds
- Hamster's appearance changes based on its condition:
  - 100-75%: Happy 😊
  - 74-50%: Normal 😐
  - 49-25%: Sad 😟
  - Below 25%: Dying 😵

## Requirements
- Python 3.8+
- `requirements.txt`