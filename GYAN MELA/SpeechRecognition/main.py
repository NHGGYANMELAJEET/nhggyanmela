import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import time
import pyautogui
import command_list
import json

# Define variables
engine = pyttsx3.init()
listener = sr.Recognizer()

print('program has started');

def getWeather(city_name):
    API_KEY = "f354c11eb850918547081c684e06e42d"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    city = city_name
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'] 
        temperature = round(data["main"]["temp"] - 273.15, 2)

        return weather, temperature
    else:
        return 0


def getTime():
    t = time.localtime()
    current_time = time.strftime("%I,%M", t)
    return current_time


def getDate():
    current_day = time.strftime("%b %d")
    return current_day


def findNumInText(text=''):
    res = [int(i) for i in text.split() if i.isdigit()]
    return res if len(res) > 0 else 0


def engineSay(speakText):
    engine.say(speakText)
    engine.runAndWait()


# define the countdown func.
def countdown(t:int) -> bool:
    t = t*60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        return True

    engineSay(f'Your {t} minute timer is over!')


# gets common words in two lists
def filter_word_query(list_1:list, list_2:list):
    list_1 = str(list_1).split()
    list_1_as_set = set(list_1)
    intersection = list(list_1_as_set.intersection(list_2))
    print(intersection)
    for word in range(len(intersection)):
        list_1.remove(intersection[word])
    return list_1


def list_to_string(list_para1:list) -> str:
    string = ''
    return string.join(list_para1)


def play_spotify():
    url_spotify = 'https://open.spotify.com/'
    webbrowser.get().open(url_spotify)
    time.sleep(9)
    pyautogui.press('space')

engineSay('Hi How may i help you?')
print('All of the functions have loaded')

def main():
    _ = True;
    while _:
        with sr.Microphone() as source:
            # adjusting for background noise
            print('microphone detected')
            listener.adjust_for_ambient_noise(source, 0.6)
            print('listener ambient noise adjusted')
            command = listener.listen(source, phrase_time_limit=2)
            print('listener activated')
            try:
                # listening the command
                text = listener.recognize_google(command)
                print('Im listening..')
                print(text)
                if 'play' in text:
                    url_youtube = 'https://www.youtube.com/results?search_query='
                    search_query_youtube = str(filter_word_query(text, command_list.commands))  # i have no idea i
                    # forgot how this works, even though i made it xDDDDDDDDDD
                    if 'spotify' not in search_query_youtube:
                        engineSay(f'playing: {search_query_youtube}')
                        webbrowser.get().open(url_youtube + search_query_youtube)
                        time.sleep(4)
                        pyautogui.press(
                            'tab')  # Using pyauto gui to play YouTube, duh what else do you think we are gonna do>??
                        pyautogui.press('enter')
                    play_spotify()
                        
                if 'weather' in text:
                    city = 'Bengaluru'
                    weather_list = getWeather(city)  # pretty straight forward if u ask me
                    if weather_list != 0:
                        engineSay(f'The weather of {city} is {weather_list[0]} and temperature is {weather_list[1]}')

                if 'stop' in text:
                    break

                if 'time' in text or 'Time' in text:
                    current_time = getTime()  # yea if you are reading this, then you probably are one heck of an idiot
                    # xD and if its me from the future, its 17/9/22 at 9.04 and my science exam is on monday and i have
                    # did studying, that what i think anyway xD
                    engineSay(f'The current time is {current_time}')

                if 'day' in text or 'Day' in text or 'date' in text or 'Date' in text:
                    current_day = getDate()  # Bruh, dont expect to find anything in these comments
                    engineSay(f'Today is {current_day}')    

                if 'how to' in text or 'why' in text:
                    search_query_google = text
                    engineSay(f'Results for {search_query_google}')
                    url = f'https://www.google.com/search?q={search_query_google}&sxsrf=ALiCzsZcvIpOyLPFaZa_huKZJA0dO5JDhA%3A1662896136188&ei=CMgdY-GQC77y4-EPtP6p2Ac&ved=0ahUKEwjhtPvr0oz6AhU--TgGHTR_CnsQ4dUDCA4&uact=5&oq=how+to+cook&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAEJECMgUIABCRAjIFCAAQkQIyBQgAEJECMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQgAQQsQM6CggAEEcQ1gQQsAM6BAgAEEdKBQg8EgExSgQIQRgASgQIRhgAULgFWI8HYPAIaAFwAngAgAHtAogB7QKSAQMzLTGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
                    webbrowser.get().open(url)  # using webbrowser to open a new tab

                if 'open' in text:
                    with open('app_names.json') as file:
                        data = json.load(file)
                        # looping through each type of app and then using lists slicing to get the commands and names
                        for i in range(len(data['apps'])):
                            name = data['apps'][i]['name']
                            if name in text:
                                engineSay(f'Opening.. {name}')
                                url = data['apps'][i]['url']
                                webbrowser.get().open(url)
                        for i in range(len(data['apps_tbo'])):
                            name = data['apps_tbo'][i]['name']
                            if name in text:
                                engineSay(f'Opening.. {name}')
                                command = data['apps_tbo'][i]['command']
                                pyautogui.hotkey('win', 'r')
                                pyautogui.typewrite(command)
                                pyautogui.press('enter')
                    print('over')

                if 'exit' in text:
                    engineSay('exitting current tab')
                    pyautogui.hotkey('alt', 'f4')  # are you kidding me?

                if 'volume down' in text:
                    nums_volume_down = findNumInText(text)
                    print(nums_volume_down)
                    if nums_volume_down != 0:
                        volume_to_shift = nums_volume_down[0]
                        engineSay(f'Sure! turning volume down by {volume_to_shift}')  # using pyautogui.. again
                        num_press_keydown = int(volume_to_shift * 1)
                        pyautogui.press('volumedown', num_press_keydown)

                if 'volume up' in text:
                    nums_volume_up = findNumInText(text)
                    print(type(text))
                    print(nums_volume_up)
                    if nums_volume_up != 0:
                        volume_to_shift_up = nums_volume_up[0]
                        engineSay(
                            f'Sure! turning volume up by {volume_to_shift_up}')  # IM LITERALLY GOING CRAZY
                        # I SHOULD BE STUDYING
                        num_press_volume_up = int(volume_to_shift_up * 1)
                        pyautogui.press('volumeup', num_press_volume_up)

                if 'close' in text and 'tab' in text:
                    num_close_tab = findNumInText(text)
                    if num_close_tab == 0:
                        pyautogui.hotkey('ctrl', 'w')
                        time.sleep(1)
                    else:  # huh, piece of mind, just close x number of tabs
                        for i in range(int(num_close_tab[0])):
                            pyautogui.hotkey('ctrl', 'w')             

                if 'program' in text:
                    _ = False   

            # some shit if i messed up
            except sr.UnknownValueError:
                print('Sorry, u spoke too bad not my problem hehe')
            except sr.WaitTimeoutError:
                print('Time out error')
            except sr.RequestError:
                print('request error')

if __name__ == "__main__":
    main()