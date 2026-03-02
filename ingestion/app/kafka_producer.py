from confluent_kafka import Producer
import json

class KafkaProducer:
    def __init__(self, host, port, logger):
        self.host = host
        self.port =  port
        self.logger = logger

    def set_producer(self):
        self.producer = Producer({
            "bootstrap.servers": f"{self.host}:{self.port}"
        })
        self.logger.info("producer is set")
        return self.producer

    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
            
    def produce_to_kafka(self, data, topic_name):
        data = json.dumps(data)
        self.producer.produce(
            topic= topic_name,
            value= data,
            callback= self.delivery_callback
        )
        self.logger.info(f"value: {data} sent to topic {topic_name}")
        self.producer.poll(0)
        self.producer.flush()

        