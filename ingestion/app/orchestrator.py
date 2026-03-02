from pathlib import Path

class Orchesrator:
    def __init__(self, logger, metadata_extractor, producer):
        self.logger = logger
        self.metadata_extractor = metadata_extractor
        self.producer = producer

    def run(self, directory_path, topic_name):
        self.directory_path = Path(directory_path)
        for file_path in self.directory_path.iterdir():
            metadata = self.metadata_extractor.get_metadata(file_path)
            result = {
                "metadata": metadata,
                "file_path": str(file_path)
            }
            self.producer.produce_to_kafka(result, topic_name)

