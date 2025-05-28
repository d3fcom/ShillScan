
from app import app
from utils import generate_mock_data
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Generate initial mock data
    try:
        generate_mock_data()
        logger.info("Application started with mock data")
    except Exception as e:
        logger.error(f"Failed to generate mock data: {e}")
    
    app.run(host="0.0.0.0", port=5000)
