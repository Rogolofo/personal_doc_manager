from pathlib import Path
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt
from datetime import datetime
from typing import List, Optional

from models.tag import Tag
from src.enums.document_categories import DocumentCategory
from src.models.person import Person


class Document(BaseModel):
    """
    Represents a document with various attributes.

    Attributes:
        title (str): The title of the document.
        file_path (Path): The file path of the document.
        category (List[DocumentCategory]): Categories the document belongs to.
        tags (Optional[List[str]]): Tags associated with the document.
        persons (Optional[List[Person]]): Persons related to the document.
        pages (NonNegativeInt): Number of pages in the document.
        created_at (datetime): The creation date and time of the document.
    """
    file_name: str
    file_type: str
    file_path: Path
    category: List[DocumentCategory]
    tags: Optional[List[Tag]] = Field(default_factory=list)
    persons: Optional[List[Person]] = Field(default_factory=list)
    pages: NonNegativeInt = Field(default=1, ge=1)
    created_at: datetime = Field(default_factory=datetime.now)
