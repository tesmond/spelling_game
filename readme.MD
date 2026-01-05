# Spelling Game

A simple spelling game that speaks a word, provides its definition, and asks you to spell it correctly.

## Features

- **Text-to-Speech**: Uses text-to-speech to pronounce words
- **Dictionary Options**: Choose between a downloaded comprehensive dictionary or a built-in fallback dictionary
- **Customizable Settings**: Adjust number of questions, minimum/maximum word lengths, and dictionary source
- **Audio Feedback**: Plays success/error sounds for correct/incorrect answers
- **Progress Tracking**: Shows current question number and score
- **Results Screen**: Displays final score and detailed results for all questions

## Dictionary Sources

- **Downloaded Dictionary**: Comprehensive word list from https://github.com/wordset/wordset-dictionary (requires internet connection)
- **Fallback Dictionary**: Built-in collection of common words (works offline)

## How to Play

1. The game speaks a word and displays its definition
2. Type your spelling in the text box
3. Press Enter or click Submit to check your answer
4. Click the replay button (🔊) to hear the word again
5. Complete all questions to see your final score and detailed results

## Settings

Access settings from the Game menu:

- **Number of Questions**: Set how many words to spell (5-20, default: 10)
- **Minimum Word Length**: Set the shortest word length (3-15, default: 5)
- **Maximum Word Length**: Set the longest word length (3-15, default: 7)
- **Use Downloaded Dictionary**: Toggle between downloaded dictionary (requires internet) or fallback dictionary (default: fallback)

## System Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Internet connection (for downloading dictionary and initial setup)
- Audio output for text-to-speech and sound effects

## Installation

1. Clone or download the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python spelling_game.py`

## Dependencies

- tkinter (standard library)
- json, urllib, gzip (standard library)
- edge-tts (Microsoft Edge neural text-to-speech)
- pygame (audio playback)
- playsound3 (sound effects)

## Controls

- **Enter**: Submit answer
- **Replay Button**: Hear the word again
- **Menu > Game > New Game**: Start a new game
- **Menu > Game > Settings**: Open settings dialog
- **Menu > Game > Exit**: Close the application