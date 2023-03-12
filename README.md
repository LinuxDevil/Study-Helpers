
# Helper Python Scripts for Bash

This repository contains a collection of Python scripts that can be used in conjunction with Bash scripts to aid in various tasks, such as studying, productivity, and automation.

## Pomodoro Script

The `pomodoro` script is a Python script that implements the Pomodoro Technique, a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. The script allows you to specify the number of Pomodoro cycles to run and the end timer sound file to play.

### Usage

To use the `pomodoro` script, you can run the `pomodoro.sh` Bash script provided in the repository:

bashCopy code

`./pomodoro.sh` 


This will start a Pomodoro timer with 4 cycles and play the `crowd.mp3` sound file at the end of each cycle and break. You can adjust the number of cycles and the end timer sound file by editing the `pomodoro.sh` script or by passing command-line arguments to the `pomodoro.py` script directly.

### Files

-   `pomodoro.py`: The Python script that implements the Pomodoro timer logic.
-   `pomodoro.sh`: A Bash script that runs the `pomodoro.py` script with default options.
-   `sounds/`: A directory containing sound files that can be played at the end of each Pomodoro cycle and break.

## Lofi Script

The Lofi script is a Python script that will play the Lofi music for you in the background!

### Usage

To use the `lofi-music.py` script, you can run it like this:

`python study_music.py --option`

Options: 
1. --play
2. --stop


## Aliases Script

The `aliases.sh` script is a Bash script that defines a set of useful aliases for common Bash commands and scripts. The aliases include commands to navigate the file system, search for files, and run Python scripts.

### Usage

To use the `aliases.sh` script, you can run it in your Bash terminal:

bashCopy code

`source aliases.sh` 

Or

`./aliases.sh`

This will define the aliases for the current terminal session. You can also add this command to your `.bashrc` file to make the aliases available every time you open a new terminal.

### Files

-   `aliases.sh`: A Bash script that defines a set of useful aliases.

## Contributing

Feel free to contribute to this repository by adding new Python scripts or improving the existing ones. Please submit a pull request with your changes, and make sure to include documentation and usage instructions for any new scripts.