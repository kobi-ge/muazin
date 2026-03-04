import logging
import os
from pathlib import Path
from dotenv import load_dotenv

from config import Config
from metadata import MetadataExtractor
from orchestrator import Orchesrator
from kafka_producer import KafkaProducer

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

config = Config(host=os.getenv("KAFKA_HOST"), port=os.getenv("KAFKA_PORT"))
metadata_extractor = MetadataExtractor(logger=logging.getLogger(MetadataExtractor.__module__))
producer = KafkaProducer(host=config.host, port=config.port, logger= logging.getLogger(KafkaProducer.__module__))
orchestrator = Orchesrator(
    logger=logging.getLogger(Orchesrator.__module__), 
    metadata_extractor=metadata_extractor,
    producer=producer)

def main():
    producer.set_producer()
    orchestrator.run(directory_path="/app/data/podcasts", topic_name="metadata")
    producer.flush()
main()

