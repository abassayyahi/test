from exchange_apis import ExchangeAPI

class BinanceAPI(ExchangeAPI):
    BASE_URL = "https://api.binance.com/api/v3"

    # Binance-specific methods go here
    def get_ticker(self, symbol):
        endpoint = f"/ticker/price?symbol={symbol}"
        return self._send_request("GET", endpoint)

    def get_fee_structure(self):
        endpoint = "/exchangeInfo"
        return self._send_request("GET", endpoint)
