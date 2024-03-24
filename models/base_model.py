#!/usr/bin/python3
"""Define BaseModel Class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Define Template for other classes."""

    def __init__(self, *args, **kwargs):
        """Give attributes once instance is created."""
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))

                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string object."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save Object."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert to dict object."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
