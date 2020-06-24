import paho.mqtt.client as mqtt
from random import randrange
import time
from threading import Thread

	

def on_message(client,userdata,msg):
	print(msg.payload.decode())
	
def rx(client):
	client.on_message=on_message
	client.loop_forever()
def publish(client,topic):
	while True:
		client.publish(topic=topic, payload=randrange(50), qos=1, retain=False)
		time.sleep(5)



broker_url = "25.119.63.148"
broker_port = 1883
client=mqtt.Client()
client.connect(broker_url,broker_port)
client.subscribe([("casa/ledon",0),("casa/ledoff",0),("bogota/temperatura",0)])


#client.loop_start()
#client.on_message=on_message

#time.sleep(1)

#client.loop_stop()
#client.disconnect()

#if __name__=='__main__':
Thread(target=rx,args=(client,)).start()
Thread(target=publish,args=(client,"bogota/temperatura",)).start()
	









