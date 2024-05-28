import requests
from confluent_kafka import Producer
import json

def obt_atmosfera():
    try:
        url = "https://api.datos.gob.mx/v1/condiciones-atmosfericas"
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

def obt_enviar():
    datos_condiciones = obt_atmosfera()
    if datos_condiciones:
        enviar("atmospheric-conditions", datos_condiciones)
        print("Datos de condiciones atmosféricas enviados correctamente")
    else:
        print("No se pudieron obtener los datos")

if __name__ == "__main__":
    obt_enviar()
