from confluent_kafka import Consumer
from pymongo import MongoClient
import json

#Conexión con la base de datos
client = MongoClient("localhost", 27017)
db = client.Pipeline
nasa = db.nasa

consumer = None

def consumer_apod():
    global consumer
    consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'my_consumer_group', 'auto.offset.reset': 'earliest'})
    consumer.subscribe(['nasa-apod'])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("ERROR: {}".format(msg.error()))
            continue

        print('Datos recibidos en el tópico "nasa-apod": {}'.format(msg.value().decode('utf-8')))
        nasa.insert_one(json.loads(msg.value().decode('utf-8')))

    consumer.close()


if __name__ == "__main__":
    consumer_apod()

