class ProcessorConfig:
    def __init__(self, es_host, es_port, kafka_host, kafka_port, mongo_host, mongo_port, mongo_user, mongo_password, logger):
        self.es_host = es_host
        self.es_port = es_port
        self.logger = logger
        self.kafka_host = kafka_host
        self.kafka_port = kafka_port
        self.mongo_host = mongo_host
        self.mongo_port = mongo_port
        self.mongo_user = mongo_user
        self.mongo_password = mongo_password



        