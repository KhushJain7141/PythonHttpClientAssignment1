INVALIDENDPOINTS = {
"stock_invalid_param_test": {
    "method": "GET",
    "path": "/stock",
    "params": {
        "wrong_param": "test"
    }
}

}

ENDPOINTS = {
    "stock_details": {
        "method": "GET",
        "path": "/stock",
        "params": {
            "name": "Tata Steel"
        }
    },

    "industry_search": {
        "method": "GET",
        "path": "/industry_search",
        "params": {
            "query": "Steel"
        }
    },

    "historical_stats_limited": {
        "method": "GET",
        "path": "/historical_stats",
        "params": {
            "stock_name": "Tata Steel",
            "stats": "ROE"
        }
    },

    "historical_data_limited": {
        "method": "GET",
        "path": "/historical_data",
        "params": {
            "stock_name": "Tata Steel",
            "period": "1m",
            "filter": "price"
        }
    },

    "stock_target_price": {
        "method": "GET",
        "path": "/stock_target_price",
        "params": {
            "stock_id": "TATASTEEL"
        }
    }
}

