$pomodoro = 'alias pomodoro="python /path/to/pomodoro.py -c 4 -s end_timer.wav"'

if [ "$(basename $SHELL)" = "bash" ]; then
  echo $pomodoro >> ~/.bashrc
elif [ "$(basename $SELL)" = 'zsh' ]; then
  echo $pomodoro >> ~/.zshrc
else
  echo "Unknown shell..."
fi

echo 'Command Finished!'