import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_request(request):
    """Log details of the incoming API request."""
    logging.info(f"Received request: {request}")
