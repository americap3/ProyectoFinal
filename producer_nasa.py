import requests
from confluent_kafka import Producer
import json

def obt(api_key):
    try:
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")
        return None

def enviar(topic, datos):
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    def delivery_report(err, msg):
        if err is not None:
            print('ERROR: {}'.format(err))
        else:
            print('Datos entregados a: {} [{}]'.format(msg.topic(), msg.partition()))

    producer.produce(topic, value=json.dumps(datos).encode('utf-8'), callback=delivery_report)
    producer.flush()

def obt_enviar(api_key):
    datos_apod = obt(api_key)
    if datos_apod:
        enviar("nasa-apod", datos_apod)
        print("Datos de APOD enviados correctamente")
    else:
        print("No se pudieron obtener los datos")

if __name__ == "__main__":
    NASA_API_KEY = 'h1NNUOWppgbKJ3ZAvePjAchHFyNsV2obFuQfs20b'
    obt_enviar(NASA_API_KEY)

