#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from typing import TYPE_CHECKING
storage = FileStorage()
storage.reload()
