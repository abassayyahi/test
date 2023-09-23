from apis.binance_api import BinanceAPI

# Initialize the Binance API with your API key and secret
binance = BinanceAPI(api_key='YOUR_BINANCE_API_KEY', api_secret='YOUR_BINANCE_API_SECRET')

# Example usage of the Binance API
ticker = binance.get_ticker('BTCUSDT')
print(ticker)
fee_structure = binance.get_fee_structure()
print(fee_structure)
