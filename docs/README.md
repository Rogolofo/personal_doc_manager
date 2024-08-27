# Personal Document Management System (PDMS)

## Overview

The Personal Document Management System (PDMS) is a comprehensive solution for digitizing, organizing, and managing personal documents. It combines optical character recognition (OCR), machine learning for document classification, and a user-friendly web interface to streamline personal document management.

## Features (Planned)

- Document upload and OCR processing
- Intelligent document classification
- Secure storage of digital documents
- Easy search and retrieval
- Web-based user interface

## Technology Stack

- Backend: Python (FastAPI)
- Frontend: Flask (for server-side rendering)
- Databases: PostgreSQL (structured data), MongoDB (unstructured data)
- OCR: Tesseract
- Machine Learning: scikit-learn
- Task Queue: Celery with Redis
- Containerization: Docker

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Git

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/personal-doc-manager.git
   cd personal-doc-manager
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install poetry
   poetry install
   ```

4. Set up the development environment:
   ```
   ./scripts/setup_dev_env.sh
   ```

5. Start the Docker containers:
   ```
   docker-compose up -d
   ```

6. Run database migrations:
   ```
   alembic upgrade head
   ```

7. Start the development server:
   ```
   uvicorn src.pdms.api.main:app --reload
   ```

The application should now be running at `http://localhost:8000`.

## Running Tests

To run the test suite:

```
pytest
```

## Contributing

We welcome contributions to the Personal Document Management System! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue on this repository.

---

Note: This project is currently in early development. Features and setup instructions may change rapidly.