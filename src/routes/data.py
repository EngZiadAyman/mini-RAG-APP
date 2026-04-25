from fastapi import FastAPI,APIRouter, Depends, UploadFile, File, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings,Settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignals

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["apiv1", "data"]
    )

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str,
                      file: UploadFile = File(...),
                      app_settings: Settings = Depends(get_settings)):

    is_valid,result_signal = DataController().validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": result_signal
                }
            )
    project_dir_path = ProjectController().get_project_path(
        project_id=project_id)
    file_path = os.path.join(project_dir_path, file.filename)

    async with aiofiles.open(file_path, "wb") as F:
        while content := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
            await F.write(content)
                
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": ResponseSignals.FILE_UPLOAD_SUCCESS.value,
                "file_path": file_path
                }
            )
        