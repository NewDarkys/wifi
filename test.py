from playsound import playsound
from threading import Thread

t = Thread(target=playsound, args=("sound.mp3",))
t.start()
