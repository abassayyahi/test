from exchange_apis import ExchangeAPI

class KuCoinAPI(ExchangeAPI):
    BASE_URL = "https://api.kucoin.com/api/v1"

    def get_ticker(self, symbol: str) -> dict:
        """Retrieve the ticker price for a given symbol from KuCoin."""
        endpoint = f"/market/orderbook/level1?symbol={symbol}"
        return self._send_request("GET", endpoint)

    def get_fee_structure(self) -> dict:
        """Retrieve the user info, which may include fee details, from KuCoin."""
        endpoint = "/user/info"
        return self._send_request("GET", endpoint)
