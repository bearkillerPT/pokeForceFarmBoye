import time
import requests
import pydirectinput
import pyautogui

# Replace with your Gotify server URL and application token
gotify_url = 'http://localhost:80'
app_token = 'APJQrj78re2CzhV'

blizzardDiedDownImage = 'botImages/blizzardDiedDown.png'

def goInAndCaptureArticuno():
    pydirectinput.keyDown('w')
    time.sleep(10)
    pydirectinput.keyUp('w')
    pydirectinput.press('q')
    time.sleep(1)
    pydirectinput.press('space')
    time.sleep(1)
    pydirectinput.press('space')
    time.sleep(2)
    
def goBackToTheEntrance():
    pydirectinput.keyDown('s')
    time.sleep(8)
    pydirectinput.keyUp('s')

def notify(msg):
     # Send the notification
    response = requests.post(f'{gotify_url}/message?token={app_token}', json=msg)
    # Check if the notification was sent successfully
    if response.status_code != 200:
        print(f'Error sending notification: {response.text}')

while True:
    while pyautogui.locateOnScreen(blizzardDiedDownImage, confidence=.7, grayscale=True) == None:
        time.sleep(.25)
    goInAndCaptureArticuno()
    notify({
        'title': 'Blizzard died down',
        'message': 'Blizzard died down',
        'priority': 5
    })
    goBackToTheEntrance()