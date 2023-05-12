const PubNub = require('pubnub');

const pubnub = new PubNub({
  publishKey: 'pub-c-',
  subscribeKey: 'sub-c-',
  userId: "myUniqueUserId"
});

const message = {
  text: 'Hello there!'
};

pubnub.publish({
  channel: 'my_channel',
  message: message,
}, function(status, response) {
  if (status.error) {
    console.log('Publish error:', status);
  } else {
    console.log('Published message:', message);
  }
});
