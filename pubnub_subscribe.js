const PubNub = require('pubnub');

const pubnub = new PubNub({
  subscribeKey: 'sub-c-',
  userId: "myUniqueUserId"

});

pubnub.addListener({
  message: function(message) {
    console.log('Received message:', message);
  },
  error: function(error) {
    console.log('PubNub error:', error);
  }
});

pubnub.subscribe({
  channels: ['my_channel'],
  withPresence: true
});
