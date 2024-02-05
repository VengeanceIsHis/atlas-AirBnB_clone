#!/usr/bin/python3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
