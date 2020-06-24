import tweepy
import paho.mqtt.client as mqtt
import time

API_key='5UC24FVp7SZobjotgf4ddMHDD'
API_secret_key='etZcWezCh9QrNeSUmM8OpuHiiMqoKrFdiHKq0AqGyYEOKJJajd'
Access_token='728052118893023233-YhqdojpmzBePnK9CnzszMx5jkVnSqbe'
Access_token_secret='UGWw0tQ23DWGp30lWAyxdcA0eyQRMWID3DoQjiqqfGSoL'
auth=tweepy.OAuthHandler(API_key,API_secret_key)
auth.set_access_token(Access_token,Access_token_secret)

api=tweepy.API(auth)


tweet_anterior=''
tweet_actual=''
broker_url = "localhost"
broker_port = 1883

notificacion=''
cont=0
start=time.time()
try:
    
	while True:
		c = tweepy.Cursor(api.search, q='#coronavirus',tweet_mode="extended").items(500)
		client = mqtt.Client()
		client.connect(broker_url, broker_port)
		client.subscribe([("twitter/notificacion",0),("twitter/tweet",0),("twitter/conteo",0)], qos=1)
		for twt in c:
			tweet_actual=twt.full_text
			#print(twt)

			if tweet_actual!=tweet_anterior:
				cont+=1
				notificacion="hay un nuevo tweet"
				print("hay un nuevo tweet")
				print(tweet_actual)
				client.publish(topic="twitter/tweet",payload=tweet_actual,qos=1,retain=False)
				time.sleep(0.5)
				tweet_anterior=tweet_actual

			else:
				notificacion="No hay nuevo tweet"
				print("No hay nuevo tweet")
			client.publish(topic="twitter/notificacion", payload=notificacion, qos=1, retain=False)
			if time.time()-start>60:
				client.publish(topic="twitter/conteo",payload=cont,retain=False)
				cont=0
				start=time.time()
				print("ha pasado un minuto")
			time.sleep(5)
except KeyboardInterrupt:
	pass
client.loop_stop()
client.disconnect()

	
	