import speech_recognition as sr
import argparse
import os

def generate_transcript(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        transcript = r.recognize_google(audio)

    return transcript

def save_transcript(transcript, file_name):
    with open(file_name, 'w') as f:
        f.write(transcript)

def main():
    parser = argparse.ArgumentParser(description='Generate Transcript from Video')
    parser.add_argument('filename', metavar='filename', type=str, help='The path to the video file')
    parser.add_argument('--output', metavar='output', type=str, help='The path to save the transcript file', default=None)

    args = parser.parse_args()

    transcript = generate_transcript(args.filename)

    print(transcript)

    if args.output is not None:
        save_transcript(transcript, args.output)
        print(f'Successfully generated transcript and saved it to {os.path.abspath(args.output)}')

if __name__ == '__main__':
    main()
