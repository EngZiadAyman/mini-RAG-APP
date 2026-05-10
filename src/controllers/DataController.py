from .BaseControler import BaseController
from models import ResponseSignal
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
    
    def validate_file(self, file : UploadFile):
        if file.content_type not in self.config.FILE_ALLOWED_Types:
            return False, ResponseSignal.file_type_error.value.format(file=file)
        if file.size > self.config.FILE_MAX_SIZE_MB * 1024 * 1024:
            return False, ResponseSignal.SIZE_ERROR.value.format(self=self)
        
        return True, ResponseSignal.File_validated_successfully.value
    

