import logging
import os


def setup_logger(name=__name__):
    """Set up and return a logger instance."""

    # Define the logger
    logger = logging.getLogger(name)

    # Set the logging level
    logger.setLevel(logging.DEBUG)

    # Define the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a file handler to write log messages to a file
    log_file = os.path.join(os.getcwd(), 'arbitrage_bot.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Create a stream handler to print log messages to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Add the stream handler to the logger
    logger.addHandler(stream_handler)

    return logger


if __name__ == "__main__":
    # Test the logger
    logger = setup_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
