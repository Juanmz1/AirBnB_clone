#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes: """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A class of the base model
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of the baseModel
        you will use *args,
        **kwargs arguments for the constructor of a BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation of the object
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, repr(self.__dict__))

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_obj = {}
        for key, values in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                dict_obj[key] = values.isoformat()
            else:
                dict_obj[key] = values
        dict_obj["__class__"] = type(self).__name__
        return dict_obj
