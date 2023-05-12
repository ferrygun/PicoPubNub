import urequests
import ujson

publish_key = 'pub-c-'
subscribe_key = 'sub-c-'

# define your API endpoint
pubnub_api_endpoint = f'https://ps.pndsn.com/publish/{publish_key}/{subscribe_key}/0/my_channel/0'

# define your payload
payload = {
    'message': 'Hello, PubNub!'
}

# convert payload to JSON format
json_payload = ujson.dumps(payload)

# make the API call
response = urequests.post(pubnub_api_endpoint, data=json_payload)

# check the response
if response.status_code == 200:
    print('Message published successfully.')
else:
    print(f'Error publishing message: {response.text}')


