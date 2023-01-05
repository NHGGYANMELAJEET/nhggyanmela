import time
import pyttsx3

engine = pyttsx3.Engine()

def countdown(t):
    t_orignal = t;
    t = t*60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    engine.say(f'Your {t_orignal} minute timer is over')
    engine.runAndWait()
    
    print('done')

countdown(5)