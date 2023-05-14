import urequests
import utime
import netman
import utime
from servo import Servo

country = 'SG'
ssid = ''
password = ''
wifi_connection = netman.connectWiFi(ssid,password,country)


s1 = Servo(0)       # Servo pin is connected to GP0
 
def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s1.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    



subscribe_key = 'sub-c-'
channel_name = 'my_channel'
timestamp = int(utime.time())
last_message = None

# define your API endpoint
pubnub_api_endpoint = f'https://ps.pndsn.com/v2/subscribe/{subscribe_key}/{channel_name}/0/{timestamp}'

while True:
    # make the API call
    response = urequests.get(pubnub_api_endpoint)

    # check the response
    if response.status_code == 200:
        messages = response.json()['m']
        if messages:
            new_last_message = messages[-1]
            if new_last_message != last_message:
                last_message = new_last_message
                print(f'Received message: {last_message}')
                
                text = last_message['d']['text']
                print(f'Received message: {text}')
                
                if text == 'LEFT':
                    print("Turn left ...")
                    for i in range(0,180,10):
                        servo_Angle(i)
                        utime.sleep(0.05)
                    
                if text == 'RIGHT':
                    print("Turn right ...")
                    for i in range(180,0,-10):
                        servo_Angle(i)
                        utime.sleep(0.05) 
            

        else:
            print('No new messages')
    else:
        print(f'Error subscribing to channel: {response.text}')

    # wait before making the next API call
    utime.sleep(1)

