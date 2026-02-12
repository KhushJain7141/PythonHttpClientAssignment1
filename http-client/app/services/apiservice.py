from app.core.exceptions import APIRequestError

class APIService:
    def __init__(self, http_client, endpoints, logger):
        self.http_client = http_client
        self.endpoints = endpoints
        self.logger = logger

    def execute_all(self):
        results = []

        for name, config in self.endpoints.items():
            try:
                result = self.http_client.send_request(
                    method=config["method"],
                    endpoint=config["path"],
                    params=config.get("params")
                )

                results.append({
                    "api": name,
                    "request": config,
                    "result": result
                })

            except APIRequestError as e:
                results.append({
                    "api": name,
                    "error": str(e)
                })

        return results
