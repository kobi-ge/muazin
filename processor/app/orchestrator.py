from unique_id import generate_unique_id
from utils import extract_fields, set_mapping


class ProcessorOrchestrator:
    def __init__(self, logger, consumer, elastic, mongo):
        self.logger = logger
        self.consumer = consumer
        self.elastic = elastic
        self.mongo = mongo

    def run(self, index_name):
        while True:
            message = self.consumer.consume()
            path, ctime, size, metadata = extract_fields(message)
            new_id = generate_unique_id(path, ctime, size)
            self.elastic.insert(index_name, metadata, new_id)
            self.logger.info(f"message: {message} inserted to elastic")

    def init_svcs(self, topic_name, index_name):
        self.consumer.set_consumer(topic_name)
        self.elastic.connect()
        self.elastic.create_index(index_name, set_mapping())
