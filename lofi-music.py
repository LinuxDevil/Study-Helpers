import argparse
import webbrowser
from random import choice

LOFI_MUSIC_URLS: list[str] = [ "https://www.youtube.com/watch?v=jfKfPfyJRdk",
                               "https://www.youtube.com/watch?v=GqnYz3Ty3Qc",
                               "https://www.youtube.com/watch?v=mxH_9dlUntU",
                               "https://www.youtube.com/watch?v=KJFWkgrwxJQ"]


def main():
    parser = argparse.ArgumentParser(description='Play Lofi Music')
    parser.add_argument('--play', action='store_true', help='Play the lofi music')
    parser.add_argument('--stop', action='store_true', help='Stop the lofi music')
    args = parser.parse_args()

    if args.play:
        webbrowser.open(choice(LOFI_MUSIC_URLS), new=1)

    if args.stop:
        for handle in webbrowser._tryorder:
            if handle.name == 'chrome':
                handle.popen.kill()

if __name__ == '__main__':
    main()
