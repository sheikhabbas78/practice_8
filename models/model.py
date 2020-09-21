from typing import Dict, TypeVar, List
from abc import ABCMeta, abstractmethod

from common.database import Database

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def find_one_by(cls, attribute: str, value: str) ->T:
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls, attribute: str, value: str) -> List[T]:
        elements = Database.find_many(cls.collection, {attribute: value})
        return [cls(**element) for element in elements]

    @classmethod
    def find_one_by_id(cls, _id) ->T:
        return cls.find_one_by("_id", _id)

    @classmethod
    def find_all(cls) -> List[T]:
        elements = Database.find_many(cls.collection, {})
        return [cls(**element) for element in elements ]

    def save_to_mongo(self) ->None:
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self) -> None:
        Database.remove(self.collection, {"_id": self._id})

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError
