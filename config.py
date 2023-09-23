import os

# API KEYS
KUCOIN_API_KEY = os.environ.get('KUCOIN_API_KEY', 'YOUR_KUCOIN_API_KEY_DEFAULT')
KUCOIN_API_SECRET = os.environ.get('KUCOIN_API_SECRET', 'YOUR_KUCOIN_API_SECRET_DEFAULT')
KUCOIN_API_PASSPHRASE = os.environ.get('KUCOIN_API_PASSPHRASE', 'YOUR_KUCOIN_API_PASSPHRASE_DEFAULT')

BINANCE_API_KEY = os.environ.get('BINANCE_API_KEY', 'YOUR_BINANCE_API_KEY_DEFAULT')
BINANCE_API_SECRET = os.environ.get('BINANCE_API_SECRET', 'YOUR_BINANCE_API_SECRET_DEFAULT')

# DATABASE CONFIGURATION
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('DB_PORT', 5432))
DB_USER = os.environ.get('DB_USER', 'your_db_username_default')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_db_password_default')
DB_NAME = os.environ.get('DB_NAME', 'your_db_name_default')

# OTHER SETTINGS
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')
ARBITRAGE_THRESHOLD = float(os.environ.get('ARBITRAGE_THRESHOLD', 0.01))
