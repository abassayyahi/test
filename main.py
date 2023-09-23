import logging
import config
from strategies.simple_arbitrage import simple_arbitrage_strategy
from exchanges.kucoin import KuCoinExchange
from exchanges.binance import BinanceExchange  # Add more exchange imports as needed

def main():
    # Set up logging
    logging.basicConfig(level=config.LOGGING_LEVEL)

    # Initialize exchanges with API keys from config
    kucoin = KuCoinExchange(api_key=config.KUCOIN_API_KEY, api_secret=config.KUCOIN_API_SECRET,
                            passphrase=config.KUCOIN_API_PASSPHRASE)
    binance = BinanceExchange(api_key=config.BINANCE_API_KEY, api_secret=config.BINANCE_API_SECRET)

    # Add more exchanges here as needed
    # Example: coinbase_pro = CoinbaseProExchange(api_key=..., api_secret=..., passphrase=...)

    # Create a list of exchanges to consider for arbitrage
    exchanges = [kucoin, binance]  # Add more exchanges here

    try:
        simple_arbitrage_strategy(exchanges)
        # Add other bot operations or strategies here
    except Exception as e:
        logging.error(f"Bot encountered an error: {e}")

if __name__ == "__main__":
    main()
