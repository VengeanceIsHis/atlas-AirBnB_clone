#!/usr/bin/python3
import os
import json
from models.base_model import BaseModel

class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
    __file_path (str): The name of the  file to save objects to.
    __objects (dict): A dictioanry of insstantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __path_path to __objects, if it exists."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                objdict = json.load(file)
                for key, value in objdict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)

                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
