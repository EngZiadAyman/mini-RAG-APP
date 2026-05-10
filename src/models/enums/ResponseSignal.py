from enum import Enum

class ResponseSignal(Enum):

    File_uploaded_successfully = "File uploaded successfully"
    File_validated_successfully = "File validated successfully"
    File_uploaded_failed = "File uploaded failed"
    File_validated_failed = "File validated failed"
    SIZE_ERROR = "File size exceeds the maximum limit of {self.config.FILE_MAX_SIZE_MB} MB"
    file_type_error = "File type {file.content_type} is not allowed."