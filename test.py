import subprocess
import re

output = subprocess.check_output(['termux-clipboard-get'])
match = re.search('level=(-?\d+)', output.decode())
if match:
    signal_strength = int(match.group(1))
    print(signal_strength)
else:
    print('Невозможно получить мощность сигнала.')