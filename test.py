import subprocess

output = subprocess.check_output(['termux-wifi-scaninfo'])
signal_strength = int(output.split()[7])
print(signal_strength)
