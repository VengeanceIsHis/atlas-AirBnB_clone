#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.base_model import BaseModel
storage = FileStorage()
storage.reload()
