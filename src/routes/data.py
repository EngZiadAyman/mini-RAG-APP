import os

from fastapi import FastAPI ,APIRouter,Depends, UploadFile, status
from helpers.config import Config, get_config
from controllers import DataController, ProjectController
from fastapi.responses import JSONResponse
import aiofiles
from models.enums.ResponseSignal import ResponseSignal

data_controller = DataController()
project_contrloller = ProjectController()

router_app = APIRouter()
@router_app.post("/upload/{project_id}")
async def upload(project_id: str,file: UploadFile,
                  config: Config = Depends(get_config)):
    is_valid, message = data_controller.validate_file(file)
    if not is_valid:
        return JSONResponse(content={"message": message},
                             status_code=status.HTTP_400_BAD_REQUEST)

    # Process the file (e.g., save it, extract content, etc.)
    # For demonstration, we will just return a success message.
    project_path = project_contrloller.get_project_path(project_id)
    file_location = os.path.join(
            project_path,
            file.filename
        )
    
    async with aiofiles.open(file_location, 'wb') as out_file:
        while chunk := await file.read(config.FILE_CHUNK_SIZE):  # Read the file in chunks
            await out_file.write(chunk)



    return JSONResponse(content={"message": ResponseSignal.File_uploaded_successfully.value,
                         "project_id": project_id,
                         "file_name": file.filename,
                         "file_location": file_location,
                         }
)