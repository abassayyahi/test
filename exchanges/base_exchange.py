import requests
import logging
import os

class BaseExchange:
    BASE_URL = ""
    HEADERS = {"Content-Type": "application/json"}

    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key or os.environ.get('EXCHANGE_API_KEY')
        self.api_secret = api_secret or os.environ.get('EXCHANGE_API_SECRET')

    def _generate_signature(self, params):
        raise NotImplementedError

    def _send_request(self, method, endpoint, params=None, private=False):
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.HEADERS.copy()

        if private:
            params = self._add_private_params(params)
            headers.update(self._get_private_headers())

        response = requests.request(method, url, headers=headers, params=params)

        if response.status_code != 200:
            logging.error(f"Error {response.status_code}: {response.text}")
            return None

        try:
            return response.json()
        except ValueError:
            logging.error(f"Invalid JSON response from {endpoint}: {response.text}")
            return response.text

    def _add_private_params(self, params):
        raise NotImplementedError

    def _get_private_headers(self):
        raise NotImplementedError
