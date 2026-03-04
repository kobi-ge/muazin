from confluent_kafka import Consumer
import json

class KafkaConsumer:
    def __init__(self, host, port, logger):
        self.host = host
        self.port = port
        self.logger = logger

    def set_consumer(self, topic_name):
        self.consumer = Consumer({
            'bootstrap.servers': f"{self.host}:{self.port}",
            'group.id': "team-metadata",   
            'auto.offset.reset': 'earliest'
        })
        self.consumer.subscribe([topic_name])
        return self.consumer
    
    def consume(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    self.logger.error("ERROR: %s".format(msg.error()))
                    continue
                value = msg.value().decode('utf-8')
                self.logger.info("Consumed event from topic {topic}: value = {value:12}".format(
                    topic=msg.topic(), value=msg.value().decode('utf-8')))
                return json.loads(value)
        except KeyboardInterrupt:
            pass

