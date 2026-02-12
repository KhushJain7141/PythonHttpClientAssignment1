import requests
from app.core.exceptions import APIRequestError


class HttpClient:
    def __init__(self, base_url, headers, api_key, timeout, logger):
        self.base_url = base_url
        self.timeout = timeout
        self.logger = logger

        self.session = requests.Session()

        
        if headers:
            self.session.headers.update(headers)


        self.session.headers.update({
            "X-Api-Key": api_key
        })

    def send_request(self, method, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"

        try:
            self.logger.info(f"{method} {url} | params={params}")

            response = self.session.request(
                method=method,
                url=url,
                params=params,
                timeout=self.timeout
            )

            status_code = response.status_code
            content_type = response.headers.get("Content-Type", "")

            self.logger.info(f"Response received | Status: {status_code}")

     
            if "application/json" in content_type.lower():
                try:
                    data = response.json()
                except ValueError:
                    data = {"error": "Invalid JSON response"}
            else:
                data = {
                    "error": "Non-JSON response",
                    "raw_response": response.text[:300] 
                }


            if 200 <= status_code < 300:
                return {
                    "status": "success",
                    "status_code": status_code,
                    "data": data
                }

            elif 400 <= status_code < 500:
                return {
                    "status": "client_error",
                    "status_code": status_code,
                    "error": data
                }

            elif 500 <= status_code < 600:
                return {
                    "status": "server_error",
                    "status_code": status_code,
                    "error": data
                }

            else:
                return {
                    "status": "unknown_status",
                    "status_code": status_code,
                    "error": data
                }

        except requests.exceptions.Timeout:
            self.logger.error("Request timed out")
            return {
                "status": "timeout_error",
                "error": "Request timed out"
            }

        except requests.exceptions.ConnectionError:
            self.logger.error("Connection error")
            return {
                "status": "connection_error",
                "error": "Failed to connect to API server"
            }

        except requests.exceptions.RequestException as exc:
            self.logger.error(f"Request exception: {exc}")
            return {
                "status": "request_exception",
                "error": str(exc)
            }

        except Exception as exc:
            self.logger.error(f"Unexpected error: {exc}")
            return {
                "status": "unexpected_error",
                "error": str(exc)
            }
