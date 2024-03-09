#!/usr/bin/python3
"""Defines a Base Class for other sub-classes"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Base class defines all common attributes and methods for other classes
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Initializes instance attributes."""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current datetime"""

        self.updated_at = datetime.now()
        model.storage.save()

    def to_dict(self):
        """returns keys/values of __dict__ of instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
