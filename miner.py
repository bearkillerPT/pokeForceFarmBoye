import time
import requests
import pydirectinput
import pyautogui

limitSecondsToFarm = 5 * 60 * 60

successfulExtractionImage = 'botImages/successfulExtraction.png'
blizzardDiedDownImage = 'botImages/blizzardDiedDown.png'

# Replace with your Gotify server URL and application token
gotify_url = 'http://localhost:80'
app_token = 'APJQrj78re2CzhV'

def notify(msg):
     # Send the notification
    response = requests.post(f'{gotify_url}/message?token={app_token}', json=msg)
    # Check if the notification was sent successfully
    if response.status_code != 200:
        print(f'Error sending notification: {response.text}')


def mineOre():
    checkForBlizzard()
    while pyautogui.locateOnScreen(successfulExtractionImage, confidence=.7, grayscale=True) != None:
        time.sleep(.25)
    while pyautogui.locateOnScreen(successfulExtractionImage, confidence=.7, grayscale=True) == None:
        pydirectinput.press('q')
        time.sleep(.25)

def goFromTheFirstOreToTheSecond():
    pydirectinput.keyDown('a')
    time.sleep(1.2)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(.5)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(.1)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(.3)
    pydirectinput.keyUp('w')

def goFromTheSecondOreToTheThird():
    pydirectinput.keyDown('s')
    time.sleep(.7)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(4.1)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(.8)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(.8)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(.2)
    pydirectinput.keyUp('d')
    
def goFromTheThirdOreToTheFirst():
    pydirectinput.keyDown('a')
    time.sleep(.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(.8)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(.8)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(1)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(4.3)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(1.5)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(.4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(1.8)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(1.3)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(.2)
    pydirectinput.keyUp('w')

def goFromtheThirdOreToTheFourth():
    pydirectinput.keyDown('a')
    time.sleep(.1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(1.7)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(.5)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(.7)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(.1)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(.2)
    pydirectinput.keyUp('w')
    
def goFromTheFourthOreToTheFifth():
    pydirectinput.keyDown('d')
    time.sleep(1)
    pydirectinput.keyUp('d')

def goFromTheFifthOreToTheSixth():
    pydirectinput.keyDown('s')
    time.sleep(.2)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(.1)
    pydirectinput.keyUp('d')

def goFromTheSixthOreToTheFirst():
    pydirectinput.keyDown('a')
    time.sleep(1.5)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(.6)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(.4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(1.7)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('s')
    time.sleep(.8)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(.8)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(1.1)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(4.3)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(1.5)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('a')
    time.sleep(.4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(1.8)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(1.3)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(.2)
    pydirectinput.keyUp('w')
    
time.sleep(.5)
def checkForBlizzard():
    global blizzardDiedDownImage
    if pyautogui.locateOnScreen(blizzardDiedDownImage, confidence=.7, grayscale=True):
        notify({
            'title': 'Blizzard died down',
            'message': 'Blizzard died down',
            'priority': 5
        })

# Start at the southernmost mining site
start_time = time.time()
i = 0
while True:
    if time.time() - start_time > limitSecondsToFarm:
        break
    mineOre()
    goFromTheFirstOreToTheSecond()
    mineOre()
    goFromTheSecondOreToTheThird()
    mineOre()
    if i == 0:
        i = 1
        goFromtheThirdOreToTheFourth()
        mineOre()
        goFromTheFourthOreToTheFifth()
        mineOre()
        goFromTheFifthOreToTheSixth()
        mineOre()
        goFromTheSixthOreToTheFirst()
    else:
        i = 0
        goFromTheThirdOreToTheFirst()
# Return to the first ore
