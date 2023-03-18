
# Helper Python Scripts for Bash

This repository contains a collection of Python scripts that can be used in conjunction with Bash scripts to aid in various tasks, such as studying, productivity, and automation.

## Pomodoro Script

The `pomodoro` script is a Python script that implements the Pomodoro Technique, a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. The script allows you to specify the number of Pomodoro cycles to run and the end timer sound file to play.

### Usage

To use the `pomodoro` script, you can run the `pomodoro.sh` Bash script provided in the repository:

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

## Site Lighthouse

This is a Python script that runs SEO, performance, best practices, and accessibility tests on a website. It uses the `lighthouse cli` to perform these tests.

### Usage

Install the lighthouse CLI

`npm install -g lighthouse`

Install [Chrome Browser](https://www.google.com/chrome/)

To run the tests, use the following command:

`python site-lighthouse.py <website-url> -p` 

Replace `<website-url>` with the URL of the website you want to test.

The script will then perform SEO, performance, best practices, and accessibility tests on the website, and print the results to the console.

## OpenAI Question Answering CLI

This is a command-line interface (CLI) written in Python that uses the OpenAI API to generate answers to technical and code-related questions. The CLI takes a prompt text as input, along with optional arguments for the OpenAI model to use and the temperature to use for generating the answer.

### Installation

To use the OpenAI Question Answering CLI, you'll need to have Python 3 installed on your machine, along with the OpenAI Python module. You can install the OpenAI module using pip:

`pip install openai` 

Once you have Python and the OpenAI module installed, you can download the `openai_qa.py` script from this repository and save it to your computer.

### Usage

To use the OpenAI Question Answering CLI, simply run the `openai_qa.py` script from the command line, passing in the prompt text as a required argument:

`python openai_qa.py "What is a Python decorator and how does it work?"` 

This will generate an answer to the specified question using the `text-davinci-002` model and a temperature of 0.5, and print the answer to the console.

You can also specify the OpenAI model to use and the temperature by passing in optional arguments:

`python openai_qa.py "What is a Python decorator and how does it work?" --model text-curie-001 --temperature 0.3` 

This will generate an answer to the specified question using the `text-curie-001` model and a temperature of 0.3, and print the answer to the console.

#### Command-Line Options

The following command-line options are available for the OpenAI Question Answering CLI:

-   `prompt_text` (required): The prompt text for the question to generate an answer for.
-   `--model` (optional): The name of the OpenAI API model to use (default: text-davinci-002).
-   `--temperature` (optional): The temperature to use for generating the answer (default: 0.5).

## Transcript Script

The `generate_transcript.py` script is a Python script that uses the SpeechRecognition module to generate a transcript from a video. It supports various video formats and uses the Google Speech Recognition API to recognize the speech in the audio.

### Usage

To use the `generate_transcript.py` script, you can run it like this:

`python generate_transcript.py path/to/video.mp4`

This command will generate a transcript from the audio in the video file at the specified path and print the transcript to the console. You can also specify the path to save the transcript file using the `--output` argument, like this:

`python generate_transcript.py path/to/video.mp4 --output path/to/transcript.txt`

This command will generate the transcript and save it to the specified file path.

### Files

-   `generate_transcript.py`: The Python script that generates a transcript from a video file.

## Aliases Script

The `aliases.sh` script is a Bash script that defines a set of useful aliases for common Bash commands and scripts. The aliases include commands to navigate the file system, search for files, and run Python scripts.

### Usage

To use the `aliases.sh` script, you can run it in your Bash terminal:

`source aliases.sh` 

Or

`./aliases.sh`

This will define the aliases for the current terminal session. You can also add this command to your `.bashrc` file to make the aliases available every time you open a new terminal.

### Files

-   `aliases.sh`: A Bash script that defines a set of useful aliases.

## Contributing

Feel free to contribute to this repository by adding new Python scripts or improving the existing ones. Please submit a pull request with your changes, and make sure to include documentation and usage instructions for any new scripts.