from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException
from src.api.dependencies import get_document_service
from src.enums.document_categories import DocumentCategory
from src.services.document_service import DocumentService
from src.schemas.document import DocumentCreate, DocumentResponse


# ? Rename?
# ? Split functionality into multiple files?
# TODO: upload, download, search, list, delete, update


router = APIRouter()


@router.post(
    "/upload",
    response_model=DocumentResponse
)
async def upload_document(
        file: UploadFile = File(...),
        document: DocumentCreate = Depends(),
        document_service: DocumentService = Depends(get_document_service)
):
    # TODO: document this endpoint

    """
    Upload a new document.

    - **file**: The file to upload
    - **document**: The document metadata
    """
    # TODO: implement file upload
    try:
        contents = await file.read()
        file_path = await document_service.save_file(contents, file.filename)

        document_dict = document.dict()
        document_dict['file_path'] = file_path

        new_document = await document_service.add_document(**document_dict)
        return DocumentResponse.from_orm(new_document)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add other CRUD operations (get, update, delete, list) here










