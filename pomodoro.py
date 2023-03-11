import argparse
import time
import sys
import os


# Define the Pomodoro timer function
def pomodoro(cycles, end_sound):
    # Define the Pomodoro cycle length and break length (in seconds)
    cycle_length = 25 * 60
    break_length = 5 * 60

    # Loop through the specified number of cycles
    for cycle in range(cycles):
        # Print the start time of the cycle
        print('Starting cycle {} at {}'.format(cycle + 1, time.strftime('%H:%M:%S')))

        # Start the Pomodoro cycle timer
        start_time = time.time()
        end_time = start_time + cycle_length
        while time.time() < end_time:
            time_left = end_time - time.time()
            minutes = int(time_left // 60)
            seconds = int(time_left % 60)
            print('{:02d}:{:02d} remaining...'.format(minutes, seconds), end='\r')
            time.sleep(1)

        # Play the end timer sound
        os.system('afplay {}'.format(end_sound))

        # Print the start time of the break
        print('Starting break at {}'.format(time.strftime('%H:%M:%S')))

        # Start the break timer
        start_time = time.time()
        end_time = start_time + break_length
        while time.time() < end_time:
            time_left = end_time - time.time()
            minutes = int(time_left // 60)
            seconds = int(time_left % 60)
            print('{:02d}:{:02d} remaining...'.format(minutes, seconds), end='\r')
            time.sleep(1)

        # Play the end timer sound
        os.system('afplay {}'.format(end_sound))

    # Print the end of the Pomodoro session
    print('Pomodoro session complete!')


# Define the CLI parser
parser = argparse.ArgumentParser(description='Start a Pomodoro timer.')
parser.add_argument('-c', '--cycles', type=int, default=4, help='Number of Pomodoro cycles to run (default: 4)')
parser.add_argument('-s', '--sound', type=str, default='end_timer.wav',
                    help='End timer sound file (default: end_timer.wav)')

# Parse the arguments and start the Pomodoro timer
args = parser.parse_args()
pomodoro(args.cycles, args.sound)
