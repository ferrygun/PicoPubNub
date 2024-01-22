
import { Zoom, ZoomState } from '/Users/ferry.djaja/node_modules/zoomino/lib/zoom.js';
import PubNub from 'pubnub';

const pubnub = new PubNub({
  publishKey: "pub-c-",
  subscribeKey: "sub-c-",
  userId: "12",
});

const zoom = new Zoom();
const channel_name = "hello_world"

// add listener
const listener = {
    status: (statusEvent) => {
        if (statusEvent.category === "PNConnectedCategory") {
            console.log("Connected");
        }
    },
    message: (messageEvent) => {
        showMessage(messageEvent.message.text);
    },
    presence: (presenceEvent) => {
        // handle presence
    }
};
pubnub.addListener(listener);

// subscribe to a channel
pubnub.subscribe({
    channels: [channel_name],
});


const showMessage = async (msgContent) => {
    console.log("message: " + msgContent);
    if(msgContent === 'mute') {
    	try {
          await zoom.mute();
        } catch {
          console.log('could not mute');
        }
    } 

    if(msgContent === 'unmute') { 
    	try {
          await zoom.unmute();
        } catch {
          console.log('could not unmute');
        }
    }


}

// publish message
const publishMessage = async (message, channel) => {
    await pubnub.publish({
      channel: channel,
      message: {
        text: message   
      },
    });
}

async function start () {
	let old_state = ""
	let state_str = ""
	
	zoom.on('state-update', (state) => {
    	console.log('zoom state update %s', state);

    	if(old_state !== state) {
    		console.log("SEND");
    		old_state = state;

    		state = String(state);
    		console.log(state)

    		if(state === "Symbol(muted)")
    			state_str = "stat_muted"
    		
    		if(state === "Symbol(unmuted)") 
    			state_str = "stat_unmuted"
  
  			if(state === "Symbol(unknown)")
  				state_str = "stat_unknown"

    		publishMessage(state_str, channel_name).then(() => {

    		});

    	} 

	});

	zoom.start();
};

start();
