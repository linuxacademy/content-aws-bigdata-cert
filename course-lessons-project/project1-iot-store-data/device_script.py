import random
import json

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from datetime import date, datetime


CLIENT_NAME = "store-thermometer-seattle1"
TOPIC = "SeattleStoreTemp/1"

# Broker path is under AWS IoT > Settings (at the bottom left)
BROKER_PATH = "a25u3mz04evknr-ats.iot.us-east-1.amazonaws.com"

# RSA 2048 bit key: Amazon Root CA 1 found here:
# https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html
ROOT_CA_PATH = './AmazonRootCA1.pem'
PRIVATE_KEY_PATH = './e04047875c-private.pem.key'
CERTIFICATE_PATH = './e04047875c-certificate.pem.crt'

IoTclient = AWSIoTMQTTClient(CLIENT_NAME)
IoTclient.configureEndpoint(BROKER_PATH, 8883)
IoTclient.configureCredentials(
    ROOT_CA_PATH, 
    PRIVATE_KEY_PATH, 
    CERTIFICATE_PATH
)

# Allow the device to queue infiited messages
IoTclient.configureOfflinePublishQueueing(-1)

# Number of messages to send after a connection returns
IoTclient.configureDrainingFrequency(2)  # 2 requests/second

# How long to wait for a [dis]connection to complete (in seconds)
IoTclient.configureConnectDisconnectTimeout(10)

# How long to wait for publish/[un]subscribe (in seconds)
IoTclient.configureMQTTOperationTimeout(5) 


IoTclient.connect()
IoTclient.publish(TOPIC, "connected", 0)

now = datetime.utcnow()
now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
payload = json.dumps({
    "timestamp": now_str,
    "temperature": str(random.choice(range(65,75)))
})
IoTclient.publish(TOPIC, payload, 0)
