import logging
import os

def setup_logger(log_level):
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("API_CLIENT")
