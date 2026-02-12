# 📈 Python HTTP API Client -- Indian Stock API

## 📌 Overview

This project implements a production-style Python HTTP API client using
OOP principles to interact with the Indian Stock API.

The client: - Uses environment-based configuration (no hardcoded
secrets) - Implements structured logging - Handles API errors
gracefully - Classifies responses (2xx, 4xx, 5xx) - Writes all responses
to a JSON output file - Follows clean architecture (core, client,
services, router)

------------------------------------------------------------------------

## 🏗 Project Structure

    http-client/
    │
    ├── app/
    │   ├── core/        # Config, logger, exceptions
    │   ├── client/      # HTTP client implementation
    │   ├── router/      # API endpoints configuration
    │   ├── services/    # Business logic layer
    │   └── utils/       # File writer
    │
    ├── main.py          # Application entry point
    ├── requirements.txt
    ├── .env.example     # Sample environment config
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## 🔐 Environment Configuration

Create a `.env` file in the root directory.
Go to this URL=https://stock.indianapi.in
Login and copy the api key and add it to your .env file 
Example:

    API_BASE_URL=https://stock.indianapi.in
    API_KEY=your_api_key_here
    DEFAULT_HEADERS={"Content-Type":"application/json"}
    TIMEOUT=10
    LOG_LEVEL=INFO

⚠️ Do NOT commit your `.env` file.\
Use `.env.example` for reference.

------------------------------------------------------------------------

## ⚙️ Installation & Setup

###  Clone the Repository

``` bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```



###  Install Dependencies

``` bash
pip install requests
pip install python-dotenv
```

------------------------------------------------------------------------

## ▶️ Running the Application

From the project root:

``` bash
python main.py
```

------------------------------------------------------------------------

## 📄 Output

After execution:

### responses.json

Contains: - API name - Request details - Status classification -
Response body or structured error

### logs/app.log

Contains: - Request URLs - Status codes - Error logs - Debug information

------------------------------------------------------------------------

## 🧪 Error Handling Tests

The client gracefully handles:

  Scenario                  Expected Classification
  ------------------------- -------------------------
  Invalid Endpoint          client_error (404)
  Missing API Key           client_error (401/403)
  Invalid Query Parameter   client_error (422)
  Server Error              server_error (5xx)
  Network Failure           connection_error
  Timeout                   timeout_error

------------------------------------------------------------------------

## 🔒 Security Practices

-   API keys stored in `.env`
-   `.env` excluded via `.gitignore`
-   No hardcoded credentials
-   Configurable headers


## 📌 Author

Khush Jain\
Python HTTP API Client Assignment
