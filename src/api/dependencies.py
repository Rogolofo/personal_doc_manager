from functools import lru_cache

from src.services.document_service import DocumentService


@lru_cache()
def get_document_service() -> DocumentService:
    return DocumentService(
    )
