from dotenv import load_dotenv
import uvicorn

from src.config.config import settings


def run_server():
    load_dotenv()  # Load environment variables from .env file
    uvicorn.run(
        # ? Maybe import the app from src.api.main instead of hardcoding it here
        "src.api.app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )


if __name__ == "__main__":
    run_server()
