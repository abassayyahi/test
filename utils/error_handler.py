from utils.logger import logger


class ExchangeAPIError(Exception):
    """Base exception class for exchange API related errors."""
    pass


class RateLimitError(ExchangeAPIError):
    """Raised when rate limits are exceeded."""
    pass


class AuthenticationError(ExchangeAPIError):
    """Raised when there's an authentication issue."""
    pass


class InsufficientFundsError(ExchangeAPIError):
    """Raised when there are insufficient funds for a trade."""
    pass


class NetworkError(ExchangeAPIError):
    """Raised when there's a network-related error."""
    pass


def handle_error(error):
    """Handles the error by logging it and potentially taking other actions."""

    if isinstance(error, RateLimitError):
        logger.warning(f"Rate limit exceeded: {error}")
        # Potentially add a delay or other logic to handle rate limits

    elif isinstance(error, AuthenticationError):
        logger.error(f"Authentication error: {error}")
        # Potentially re-authenticate or notify the user

    elif isinstance(error, InsufficientFundsError):
        logger.error(f"Insufficient funds: {error}")
        # Potentially notify the user or stop trading

    elif isinstance(error, NetworkError):
        logger.error(f"Network error: {error}")
        # Potentially retry the request or check the network connection

    else:
        logger.error(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    # Test the error handler
    try:
        raise RateLimitError("Too many requests in a short time!")
    except ExchangeAPIError as e:
        handle_error(e)
