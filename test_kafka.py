from kafka import KafkaProducer

def test_kafka_connection():
    try:
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        print("Kafka connection successful")
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")

if __name__ == "__main__":
    test_kafka_connection()
 