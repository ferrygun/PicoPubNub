import urequests
import utime
import machine
from machine import Pin

publish_key = 'pub-c-'
subscribe_key = 'sub-c-'

channel_name = 'hello_world'
timestamp = int(utime.time())

# define your API endpoint
pubnub_api_endpoint = f'https://ps.pndsn.com/v2/subscribe/{subscribe_key}/{channel_name}/0/{timestamp}'

led_green = Pin(27,Pin.OUT, Pin.PULL_DOWN)
led_green.high() #off
#led_green.low() #on
led_blue = Pin(26,Pin.OUT, Pin.PULL_DOWN)
led_blue.high() #off
#led_blue.low() #on
led_red = Pin(28,Pin.OUT, Pin.PULL_DOWN)
led_red.high() #off
#led_red.low() #on


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
                #print(f'Received message: {last_message}')
                
                text = last_message['d']
                #print(f'Received message: {text}')
                print(text['text'])
                
                if text['text'] == 'stat_unmuted':
                    print("stat_unmuted ...")
                    led_green.low() #on
                    led_blue.high() #off
                    led_red.high() #off
                                        
                if text['text'] == 'stat_muted':
                    print("stat_muted ...")
                    
                    led_green.high() #off
                    led_blue.high() #off
                    led_red.low() #on
                    
                if text['text'] == 'stat_unknown':
                    print("stat_unknown ...")
                    
                    led_green.high() #off
                    led_blue.high() #off
                    led_red.high() #off
                    
            

        else:
            print('No new messages')
    else:
        print(f'Error subscribing to channel: {response.text}')

    # wait before making the next API call
    utime.sleep(0.1)
