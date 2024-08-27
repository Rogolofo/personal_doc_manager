from enum import Enum


class DocumentCategory(Enum):
    """
    Enum representing different categories of documents.
    """

    OTHER = None
    INSURANCE = "Versicherung"
    FINANCE = "Finanzen"
