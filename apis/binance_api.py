from exchange_apis import ExchangeAPI

class BinanceAPI(ExchangeAPI):
    BASE_URL = "https://api.binance.com/api/v3"

    def get_ticker(self, symbol: str) -> dict:
        """Retrieve the ticker price for a given symbol from Binance."""
        endpoint = f"/ticker/price?symbol={symbol}"
        return self._send_request("GET", endpoint)

    def get_fee_structure(self) -> dict:
        """Retrieve the fee structure from Binance."""
        endpoint = "/exchangeInfo"
        return self._send_request("GET", endpoint)
