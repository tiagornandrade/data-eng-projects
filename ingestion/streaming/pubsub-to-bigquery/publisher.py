import os
import json
from google.cloud import pubsub_v1
from generate import create_contacts
from google.oauth2 import service_account
from dotenv import load_dotenv


load_dotenv()


PROJECT_ID = os.getenv("PROJECT_ID")
TOPIC_ID = os.getenv("TOPIC_ID")
SERVICE_ACCOUNT_PATH = os.getenv("SERVICE_ACCOUNT_PATH")

CREDENTIALS = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_PATH)

publisher = pubsub_v1.PublisherClient(credentials=CREDENTIALS)
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)


while True:
    print('Generating Contacts: ')
    contacts = create_contacts(1000)
    for contact in contacts:
        publisher.publish(topic_path, data=json.dumps(contact).encode('utf-8'))
        print('Message published.')
