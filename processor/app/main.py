import os
import logging

from config import ProcessorConfig
from elastic_connection import ElasticConnection
from kafka_consumer import KafkaConsumer
from mongo_connection import MongoConnection
from orchestrator import ProcessorOrchestrator
from unique_id import generate_unique_id

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

config = ProcessorConfig(
        es_host=os.getenv("ES_HOST"), 
        es_port=int(os.getenv("ES_PORT")), 
        kafka_host=os.getenv("KAFKA_HOST"),
        kafka_port=int(os.getenv("KAFKA_PORT")),
        mongo_host=os.getenv("MONGO_HOST"),
        mongo_port=int(os.getenv("MONGO_PORT")),
        mongo_user=os.getenv("MONGO_USER"),
        mongo_password=os.getenv("MONGO_PASSWORD"),
        logger=logging.getLogger(ProcessorConfig.__module__))
consumer = KafkaConsumer(host=config.kafka_host, port=config.kafka_port, logger= logging.getLogger(KafkaConsumer.__module__))
es = ElasticConnection(host=config.es_host, port=config.es_port, logger=logging.getLogger(ElasticConnection.__module__))
mongo = MongoConnection(host=config.mongo_host, port=config.mongo_port, user=config.mongo_user, password=config.mongo_password, logger=logging.getLogger(MongoConnection.__module__))
orchestrator = ProcessorOrchestrator(consumer=consumer, elastic=es, mongo=mongo, logger=logging.getLogger(ProcessorOrchestrator.__module__))


def main():
    orchestrator.init_svcs("metadata", "audio_metadata")
    orchestrator.run("audio_metadata")

main()