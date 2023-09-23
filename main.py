import logging
import config
from strategies.simple_arbitrage import simple_arbitrage_strategy
from exchanges.kucoin import KuCoinExchange
from exchanges.binance import BinanceExchange

def initialize_exchanges():
    kucoin = KuCoinExchange(api_key=config.KUCOIN_API_KEY, api_secret=config.KUCOIN_API_SECRET)
    binance = BinanceExchange(api_key=config.BINANCE_API_KEY, api_secret=config.BINANCE_API_SECRET)
    return [kucoin, binance]

def main():
    logging.basicConfig(level=config.LOGGING_LEVEL)
    exchanges = initialize_exchanges()
    try:
        simple_arbitrage_strategy(exchanges)
    except Exception as e:
        logging.error(f"Bot encountered an error: {e}")

if __name__ == "__main__":
    main()
