import argparse
import webbrowser

LOFI_MUSIC_URL = 'https://www.youtube.com/watch?v=5qap5aO4i9A'

def main():
    parser = argparse.ArgumentParser(description='Play Lofi Music')
    parser.add_argument('--play', action='store_true', help='Play the lofi music')
    parser.add_argument('--stop', action='store_true', help='Stop the lofi music')
    args = parser.parse_args()

    if args.play:
        webbrowser.open(LOFI_MUSIC_URL, new=1)

    if args.stop:
        for handle in webbrowser._tryorder:
            if handle.name == 'chrome':
                handle.popen.kill()

if __name__ == '__main__':
    main()
