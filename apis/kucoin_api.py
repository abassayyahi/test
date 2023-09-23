from exchange_apis import ExchangeAPI


class KuCoinAPI(ExchangeAPI):
    BASE_URL = "https://api.kucoin.com/api/v1"

    # KuCoin-specific methods go here
    def get_ticker(self, symbol):
        endpoint = f"/market/orderbook/level1?symbol={symbol}"
        return self._send_request("GET", endpoint)

    def get_fee_structure(self):
        endpoint = "/user/info"
        return self._send_request("GET", endpoint)
