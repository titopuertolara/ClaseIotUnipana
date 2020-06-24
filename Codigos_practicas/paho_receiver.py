import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
def on_message(client,userdata,msg):
	
	print(msg.payload.decode())
	if(msg.payload.decode()=="ON"):
		print("Led encendido")
		GPIO.output(2,GPIO.HIGH)
	elif (msg.payload.decode()=="OFF"):
		print("Led apagado")
		GPIO.output(2,GPIO.LOW)
	
	
  
  

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

broker_url = "IP"
broker_port = 1883
client=mqtt.Client()
client.on_message=on_message
client.connect(broker_url,broker_port)
client.subscribe([("casa/ledon",0),("casa/ledoff",0)])

client.loop_forever()


