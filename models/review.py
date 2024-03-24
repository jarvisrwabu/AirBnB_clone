#!/usr/bin/python3

"""Class Review inherits from BaseModel class."""
from .base_model import BaseModel


class Review(BaseModel):
    """Inherit from SuperClass BaseModel."""

    place_id = ""
    user_id = ""
    text = ""
