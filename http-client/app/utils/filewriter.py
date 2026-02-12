import json
from datetime import datetime
from app.core.exceptions import FileWriteError

def write_json(data, filename="responses.json"):
    try:
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "results": data
        }

        with open(filename, "w") as file:
            json.dump(payload, file, indent=4)

    except Exception as exc:
        raise FileWriteError(str(exc))
