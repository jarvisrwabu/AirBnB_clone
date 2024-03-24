#!/usr/bin/python3
"""Create object storage and connect base_model.py to file_storage.py."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
