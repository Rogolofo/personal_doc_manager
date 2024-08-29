# Personal Document Management System (PDMS)

## Technology stack

FastAPI: WEB backend  
Streamlit: WEB frontend

pydantic: data validation  

MongoDB: document storage (is a NoSQL db really the best choice here?)  
PostgreSQL: metadata storage (what even is metadata in this case?)  

## Supported document types
Initially supports PDF and image

## Planned features
- Frontend to upload documents will have a button which lets you take a photo, choose an image from you gallery or upload a PDF.  
After uploading a document you have to add a category and can (optionally) add tags and persons to it.  

- The backend will then process the document and added information and store it in the database.

- The frontend will also have a search bar to search for documents.

- In a second development phase project will also use some form of machine learning to classify documents. The categories set by the user will be used as training data.

## Project Purpose

The Personal Document Management System (PDMS) is designed to help individuals digitize, organize, and manage their personal documents efficiently. It aims to solve the problem of paper clutter and make personal document retrieval quick and easy.

Key features:
- Document upload and OCR processing
- Intelligent document classification
- Secure storage of digital documents
- Easy search and retrieval
- Web-based user interface for accessibility

## Project Structure

```
personal_doc_manager/
├── pyproject.toml
├── .pre-commit-config.yaml
├── docker-compose.yml
├── src/
│   ├── pdms/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── document_processor.py
│   │   │   └── ocr.py
│   │   ├── ml/
│   │   │   ├── __init__.py
│   │   │   └── classifier.py
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── sql_models.py
│   │   │   ├── nosql_models.py
│   │   │   └── db_manager.py
│   │   ├── web/
│   │   │   ├── __init__.py
│   │   │   ├── app.py
│   │   │   └── templates/
│   │   │       ├── base.html
│   │   │       ├── index.html
│   │   │       └── document_view.html
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── decorators.py
│   │       └── context_managers.py
│   └── celery_worker.py
├── tests/
│   ├── unit/
│   │   ├── test_document_processor.py
│   │   └── test_db_manager.py
│   └── integration/
│       ├── test_api.py
│       └── test_web_interface.py
├── docs/
│   └── README.md
├── scripts/
│   ├── run_tests.sh
│   └── setup_dev_env.sh
└── alembic/
    ├── env.py
    └── versions/
        └── (migration files)
```

## Implementation Guide

1. **Set up the development environment**
   - Why: Ensures consistent development across team members
   - Tasks:
     - Create a virtual environment
     - Set up Docker for containerization
     - Configure pre-commit hooks for code quality

2. **Implement the database layer**
   - Why: Provides persistent storage for documents and metadata
   - Tasks:
     - Set up PostgreSQL for structured data (user info, document metadata)
     - Set up MongoDB for unstructured data (document contents)
     - Create database models and migrations

3. **Develop the core document processing functionality**
   - Why: Forms the backbone of the system's document handling capabilities
   - Tasks:
     - Implement OCR using libraries like Tesseract
     - Develop document classification using machine learning (scikit-learn)
     - Create a pipeline for document ingestion and processing

4. **Build the API layer**
   - Why: Enables communication between the frontend and backend
   - Tasks:
     - Design RESTful API endpoints using FastAPI
     - Implement user authentication and authorization
     - Create CRUD operations for documents

5. **Develop the web interface**
   - Why: Provides a user-friendly way to interact with the system
   - Tasks:
     - Create a Flask application for the frontend
     - Design and implement HTML templates
     - Develop user registration and login functionality
     - Create interfaces for document upload, viewing, and searching

6. **Implement background tasks**
   - Why: Handles time-consuming operations without blocking user interactions
   - Tasks:
     - Set up Celery for task queue management
     - Implement background tasks for document processing and periodic operations

7. **Enhance search functionality**
   - Why: Improves user experience in finding specific documents
   - Tasks:
     - Implement full-text search using database features
     - Develop advanced search using machine learning techniques

8. **Security enhancements**
   - Why: Protects sensitive user data
   - Tasks:
     - Implement encryption for stored documents
     - Set up secure communication (HTTPS)
     - Conduct security audits and penetration testing

9. **Testing and quality assurance**
   - Why: Ensures reliability and robustness of the system
   - Tasks:
     - Write unit tests for individual components
     - Develop integration tests for system-wide functionality
     - Perform user acceptance testing

10. **Documentation and deployment**
    - Why: Facilitates maintenance and usage of the system
    - Tasks:
      - Write comprehensive API documentation
      - Create user guides and tutorials
      - Set up CI/CD pipelines for automated testing and deployment

## Next Steps

1. Begin with setting up the development environment and project structure
2. Focus on implementing the core functionality (database, document processing)
3. Gradually build out the API and web interface
4. Continuously refine and expand features based on testing and feedback

Remember to regularly update this document as the project evolves. Good luck with your Personal Document Management System!