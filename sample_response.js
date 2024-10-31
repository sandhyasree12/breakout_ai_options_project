const sampleResponse = {
    "success": true,
    "data": {
        "options": [
            {
                "symbol": "RELIANCE21OCT2000CE",
                "expiryDate": "2024-10-21",
                "strikePrice": 2000,
                "lastPrice": 50.25,
                "bid": 49.00,
                "ask": 51.00,
                "openInterest": 1200,
                "volume": 300,
                "impliedVolatility": 0.25,
                "delta": 0.55,
                "gamma": 0.03,
                "theta": -0.02,
                "vega": 0.10
            },
            {
                "symbol": "RELIANCE21OCT2000PE",
                "expiryDate": "2024-10-21",
                "strikePrice": 2000,
                "lastPrice": 20.10,
                "bid": 19.00,
                "ask": 21.00,
                "openInterest": 800,
                "volume": 150,
                "impliedVolatility": 0.30,
                "delta": -0.45,
                "gamma": 0.02,
                "theta": -0.01,
                "vega": 0.05
            }
        ]
    },
    "message": "Data fetched successfully."
};

// Export the sample response for use in other parts of your application
module.exports = sampleResponse;
