class DocumentService:
    def __init__(self):
        self.documents = []

    def get_documents(self):
        return self.documents

    def add_document(self, document):
        self.documents.append(document)