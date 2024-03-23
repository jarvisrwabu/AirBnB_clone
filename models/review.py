#!/usr/bin/python3

"""Class Review inherits from BaseModel class."""
from .base_model import BaseModel

class Review(BaseModel):
    place_id = "" # string - empty string: it will be the Place.id
    user_id = "" # string - empty string: it will be the User.id
    text = ""
