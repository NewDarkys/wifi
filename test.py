from playsound import playsound
from threading import Thread

def t = Thread(target=playsound, args=("sound.mp3",))
t.start()
