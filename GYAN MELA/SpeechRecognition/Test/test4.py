import json
import webbrowser
import pyautogui

def engineSay(text):
    print(text)

text = str(input('What would you like to do? :: ')).split()

with open('app_names.json') as file:
    data = json.load(file)

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
            pyautogui.hotkey('win','r')
            pyautogui.typewrite(command)
            pyautogui.press('enter')
    
