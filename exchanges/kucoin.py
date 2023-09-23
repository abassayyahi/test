from apis.kucoin_api import KuCoinAPI

# Initialize the KuCoin API with your API key and secret
kucoin = KuCoinAPI(api_key='YOUR_KUCOIN_API_KEY', api_secret='YOUR_KUCOIN_API_SECRET')

# Example usage of the KuCoin API
ticker = kucoin.get_ticker('BTC-USDT')
print(ticker)
fee_structure = kucoin.get_fee_structure()
print(fee_structure)
