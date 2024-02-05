#!/usr/bin/python3
import uuid
from datetime import datetime
import unittest
import sys
from models.__init__ import storage
from models.engine.file_storage import FileStorage
class BaseModel():
    def __init__(self):
    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        storage.save(self)

    def to_dict(self):
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        rdict["id"] = self.id
        return rdict
    

if __name__ == '__main__':
    unittest.main()
