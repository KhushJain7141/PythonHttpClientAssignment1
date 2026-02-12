from app.core.config import Config
from app.core.logger import setup_logger
from app.client.httpclient import HttpClient
from app.router.endpoints import ENDPOINTS
from app.services.apiservice import APIService
from app.utils.filewriter import write_json
from app.core.exceptions import ConfigError, FileWriteError

def main():
    try:
        config = Config()
        logger = setup_logger(config.log_level)

        logger.info("Application started")

        client = HttpClient(
            base_url=config.base_url,
            headers=config.headers,
            api_key=config.api_key,
            timeout=config.timeout,
            logger=logger
        )

        service = APIService(client, ENDPOINTS, logger)
        results = service.execute_all()

        write_json(results)
        logger.info("Responses saved successfully")

    except ConfigError as e:
        print(f"Configuration Error: {e}")

    except FileWriteError as e:
        print(f"File Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
