import urequests
import utime

subscribe_key = 'sub-c-'
channel_name = 'my_channel'
timestamp = int(utime.time())

# define your API endpoint
pubnub_api_endpoint = f'https://ps.pndsn.com/v2/subscribe/{subscribe_key}/{channel_name}/0/{timestamp}'

while True:
    # make the API call
    response = urequests.get(pubnub_api_endpoint)

    # check the response
    if response.status_code == 200:
        messages = response.json()['m']
        for message in messages:
            print(f'Received message: {message}')
    else:
        print(f'Error subscribing to channel: {response.text}')

    # wait before making the next API call
    utime.sleep(1)

