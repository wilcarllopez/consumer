import os
import consumer.consumer
from consumer.consumer import setup_logging

setup_logging(default_path=os.path.join("/".join(__file__.split('/')[:-1]), 'config', 'logging_config.yml')) #added to __init__.py