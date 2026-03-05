from pymongo import MongoClient, errors
import gridfs
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

class MongoConnection:
    def __init__(self, host , port, logger):
        self.host = host
        self.port = port
        self.uri = f"mongodb://{self.host}:{self.port}"
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

    def create_fs(self):
        try:
            self.db = self.client['muazin']
            self.fs = gridfs.GridFS(self.db)
            self.logger.info(f"gridfs: {self.fs} created")
        except errors.PyMongoError as e:
            self.logger.error(f"error: {e}")

    def insert(self, data, unique_id):
        try:
            with open (data, "rb") as file:
                self.fs.put(data=file, _id=unique_id)
                self.logger.info(f"dasta: {data} inserted to mongo")
        except errors.PyMongoError as e:
            self.logger.error(f"error inserting data: {e}")


