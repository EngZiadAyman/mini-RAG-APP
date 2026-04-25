from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignals

class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignals.FILE_TYPE_NOT_SUPPORTED.value

        if getattr(file, "size", 0) > self.app_settings.FILE_MAX_SIZE:
            return False, ResponseSignals.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignals.FILE_VALIDATION_SUCCESS.value
