import pymongo
from typing import Dict


class Database:
    URI = 'mongodb://127.0.0.1:27017/fullstack'
    DATABASE = pymongo.MongoClient(URI).get_default_database()

    @staticmethod
    def find_one(collection: str, query: Dict) ->Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_many(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].save(data)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> None:
        Database.DATABASE[collection].remove(query)