import logging
import config

def fetch_prices_from_exchanges(exchanges):
    """Fetch BTC-USDT prices from all provided exchanges."""
    prices = {}
    for exchange in exchanges:
        exchange_name = type(exchange).__name__
        try:
            prices[exchange_name] = exchange.api.get_ticker('BTC-USDT')
        except Exception as e:
            logging.error(f"Error fetching price from {exchange_name}: {e}")
    return prices

def identify_arbitrage_opportunities(prices):
    """Identify arbitrage opportunities based on fetched prices."""
    for exchange_a, price_a in prices.items():
        for exchange_b, price_b in prices.items():
            if exchange_a != exchange_b and price_a and price_b:
                if price_a > price_b * (1 + config.ARBITRAGE_THRESHOLD):
                    logging.info(
                        f"Arbitrage Opportunity Found! Buy BTC on {exchange_b} at {price_b} and sell on {exchange_a} at {price_a}")
                    # ... Add logic to execute trades ...

def simple_arbitrage_strategy(exchanges):
    """
    Execute a simple arbitrage strategy across multiple exchanges.

    :param exchanges: List of exchange instances to consider for arbitrage.
    """
    prices = fetch_prices_from_exchanges(exchanges)
    identify_arbitrage_opportunities(prices)
