import cayenne.client
from random import randint
from time import sleep


def cayene(valors):
    temperatura = valors[0]
    humitat = valors[1]
    client.virtualWrite(1,temperatura,"temp","c")
    client.virtualWrite(2,humitat)

def lectura():
    temperatura = randint(10,35)
    humitat = randint(50,100)
    return temperatura,humitat


# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "2dd7a530-d092-11e8-a056-c5cffe7f75f9"
MQTT_PASSWORD = "6d63b6a30a53c35a4abd3bc1b1876c470738a485"
MQTT_CLIENT_ID = "00035950-7c78-11e9-be3b-372b0d2759ae"
client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

while True:
    client.loop()
    valors =lectura()
    cayene(valors)     
    sleep(1)









