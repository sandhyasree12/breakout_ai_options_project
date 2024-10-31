import requests
import pandas as pd

# Define API key and base URL for the Quotient API
API_KEY = "1a4b32723bmsh7e81c469b67e91ap127338jsn406e08d8124a"
BASE_URL = "https://quotient.p.rapidapi.com/options/prices"

# Define the headers for the request
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "quotient.p.rapidapi.com"
}

def get_option_chain_data(symbol, option_type, expiration, strike):
    params = {
        "symbol": symbol,
        "type": option_type,
        "expiration": expiration,
        "strike": strike,
        "min_expiry": "2024-05-21",
        "max_expiry": "2025-12-14",
        "min_strike": 50,
        "max_strike": 200
    }
    
    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        # Print the raw data for debugging
        print("Raw API response:", data)
        
        # Check if data contains options information
        if isinstance(data, list) and len(data) > 0:
            # Filter option data based on type (Call or Put)
            filtered_data = [entry for entry in data if 'Contract' in entry]
            if filtered_data:
                # Create a DataFrame
                df = pd.DataFrame(filtered_data)
                # Filter based on the option type
                if option_type.lower() == "call":
                    df = df[['Contract', 'Bid', 'Ask']].loc[df['Ask'].notnull()]
                    if not df.empty:
                        highest_ask = df.loc[df['Ask'].idxmax()]
                        return highest_ask
                elif option_type.lower() == "put":
                    df = df[['Contract', 'Bid', 'Ask']].loc[df['Bid'].notnull()]
                    if not df.empty:
                        highest_bid = df.loc[df['Bid'].idxmax()]
                        return highest_bid

            print("No valid option data found in response.")
            return pd.Series()
        
        # If a message about subscription limits is found, handle accordingly
        if 'message' in data:
            print(data['message'])
            return pd.Series()
        
    except requests.exceptions.HTTPError as err:
        print(f"API request error: {err}")
        return pd.Series()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.Series()

def calculate_margin_and_premium(option_data, quantity):
    """
    Calculate margin and premium based on option data and quantity.
    
    Parameters:
    - option_data: Series containing option data (Contract, Bid, Ask)
    - quantity: Number of options to be purchased
    
    Returns:
    - margin: Calculated margin
    - premium: Calculated premium
    """
    if option_data.empty:
        return None, None
    
    contract = option_data['Contract']
    ask_price = option_data['Ask']
    
    if pd.isna(ask_price):
        print("Ask price is not available.")
        return None, None
    
    premium = ask_price * quantity
    margin = premium * 0.2  # Example: Assuming 20% margin requirement
    
    return margin, premium

def main():
    # Example usage
    symbol = "AAPL"  # Test with a known symbol
    option_type = "Call"  # Change to "Put" if needed
    expiration = "2024-12-14"  # Ensure this is a future date
    strike = 50  # Use a realistic strike price
    quantity = 10  # Example quantity of options to be purchased

    option_data = get_option_chain_data(symbol, option_type, expiration, strike)
    print("Option Chain Data:")
    print(option_data)
    
    margin, premium = calculate_margin_and_premium(option_data, quantity)
    print(f"Margin: {margin}, Premium: {premium}")

if __name__ == "__main__":
    main()
