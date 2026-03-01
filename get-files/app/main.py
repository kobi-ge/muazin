import logging
import os

from config import Config
from metadata import MetadataExtractor
from orchestrator import Orchesrator

logging.basicConfig(level=logging.debug, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

config = Config(host=os.getenv("KAFKA_SERVICE"), port=os.getenv("KAFKA_PORT"))
metadata_extractor = MetadataExtractor(logger=logging.getLogger(MetadataExtractor.__module__))
orchestrator = Orchesrator(logger=logging.getLogger(Orchesrator.__module__), metadata_extractor=metadata_extractor)

def main():
    orchestrator.run()



