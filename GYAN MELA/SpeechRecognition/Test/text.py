import json
import time
import webbrowser
import os
import pyautogui

text = 'Hey, open word'.split()

if 'open' in text:
    f = open('app_names.json')
    data = json.load(f)
    print('open detected')
   # print(data)
    #print(data['apps'][0]['name'])
    for i in range(len(data)):
        name_app_unfiltered_normal = data['apps'][i]['name']
        name_app_unfiltered_office = data['apps_tbo'][i]['name']
        if name_app_unfiltered_normal in text:
            print('App name found')
            url = data['apps'][i]['url']
            webbrowser.get().open(url)
        elif name_app_unfiltered_office in text:
            print('Office, app!')
            command = data['apps_tbo'][i]['command']
            pyautogui.hotkey('win','r')
            time.sleep(1)
            pyautogui.typewrite(command)
            pyautogui.press('enter')

print('The code has been over')
