import requests
import hmac
import hashlib
import time
import logging

class ExchangeAPI:
    BASE_URL = ""  # To be defined in subclasses

    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key
        self.api_secret = api_secret

    def _generate_signature(self, params):
        """Generate the signature for private API calls."""
        ordered_params = sorted(params.items())
        query_string = "&".join([f"{k}={v}" for k, v in ordered_params])
        return hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    def _send_request(self, method, endpoint, params=None, private=False):
        """A generic method to send requests to the API."""
        url = f"{self.BASE_URL}{endpoint}"
        headers = {"Content-Type": "application/json"}

        if private:
            params['timestamp'] = int(time.time() * 1000)
            params['signature'] = self._generate_signature(params)
            headers["X-API-KEY"] = self.api_key

        response = requests.request(method, url, headers=headers, params=params)

        if response.status_code != 200:
            logging.error(f"Error {response.status_code}: {response.text}")
            return None

        try:
            return response.json()
        except ValueError:
            logging.error(f"Invalid JSON response from {endpoint}: {response.text}")
            return response.text
