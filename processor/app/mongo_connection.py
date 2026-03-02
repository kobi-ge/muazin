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

    def create_colection(self):
        try:
            self.db = self.client['muazin']
            self.collection = self.db['audio']
            self.logger.info(f"collection: {self.collection} created")
        except errors.PyMongoError as e:
            self.logger.error(f"error: {e}")

    def insert(self, data):
        try:
            self.client.insertOne(data)
            self.logger.info(f"dasta: {data} inserted to mongo")
        except errors.PyMongoError as e:
            self.logger.error(f"error inserting data: {e}")


