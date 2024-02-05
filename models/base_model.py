#!/usr/bin/python3
import uuid
from datetime import datetime
import unittest
import sys
from models.__init__ import storage
from models.engine.file_storage import FileStorage
class BaseModel():
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"                    
        self.is_new_instance = True
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            self.is_new_instance = False
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        if self.is_new_instance:
            storage.new(self)

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
