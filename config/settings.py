from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
MQTT_PORT = int(os.getenv('MQTT_PORT'))
MQTT_BROKER = os.getenv('MQTT_BROKER')

PUBLISH_BROKER = os.getenv('PUBLISH_BROKER')
PUBLISH_PORT = int(os.getenv('PUBLISH_PORT'))
