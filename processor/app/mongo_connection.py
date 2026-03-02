from pymongo import MongoClient, errors
import os
import logging

class MongoConnection:
    def __init__(self,host , port, user, password, logger):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}"
        self.logger = logger

    def connect(self):
        try:
            print(self.uri)
            self.client = MongoClient(self.uri)
            self.logger.info('connection established')
            return self.client
        except errors.ConnectionFailure as e:
            self.logger.error(f"error connecting to mongo: {e}")


