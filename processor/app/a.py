from pymongo import MongoClient, errors
import gridfs
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

class MongoConnection:
    def __init__(self, host , port, user, password, logger):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/?authSource=admin"
        self.logger = logger

    def connect(self):
        try:
            print(self.uri)
            self.client = MongoClient(self.uri)
            self.logger.info('connection to mongo established')
            print(self.uri)
            return self.client
        except errors.ConnectionFailure as e:
            self.logger.error(f"error connecting to mongo: {e}")
    
    def create_fs(self, file_path, unique_id):
        try:
            self.db = self.client['muazin']
            self.fs = gridfs.GridFS(self.db)
            with open(file_path, 'rb') as file_data:
                self.fs.put(file_data, filename=unique_id)
        except Exception as e:
            raise e
        
a = MongoConnection("localhost", 27017, "user", "pass", logger=logging.getLogger(MongoConnection.__module__))
a.connect()
a.create_fs(r"C:\podcasts\download (1).wav", "sdfgdsf")