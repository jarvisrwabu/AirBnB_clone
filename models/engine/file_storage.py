#!/usr/bin/python3
"""Represent an abstracted storage engine."""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os.path
import json


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        oc_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for an_o in obj_dict.values():
                    cls_name = an_o["__class__"]
                    del an_o["__class__"]
                    self.new(eval(cls_name)(**an_o))
        except FileNotFoundError:
            return
