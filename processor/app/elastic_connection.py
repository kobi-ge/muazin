from elasticsearch import Elasticsearch, ConnectionError
import logging



class ElasticConnection:
    def __init__(self, host, port, logger):
        self.host = host
        self.port = port
        self.logger = logger

    def connect(self):
        try:
            self.es = Elasticsearch(f"http://{self.host}:{self.port}")
            result = self.es.ping()

            self.logger.info("connection established: ", result)
        except ConnectionError as e:
            self.logger.error(f"error connecting to elastic: {e}")
    
    def create_index(self, index_name, mapping):
        try:
            result = self.es.indices.create(index=index_name, mappings=mapping)
            self.logger.info(f"sindex successfully created: {result}")
        except Exception as e:
            self.logger.error(f"error creating index {index_name}: {e}")



