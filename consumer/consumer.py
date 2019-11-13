import configparser
import logging
import logging.config
import os
import pika
import sys
import yaml


def setup_logging(default_path='logging_config.yml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setting up the logging config"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print('Error in Logging Configuration. Using default configs', e)
                logging.basicConfig(level=default_level, stream=sys.stdout)
    else:
        logging.basicConfig(level=default_level, stream=sys.stdout)
        print('Failed to load configuration file. Using default configs')


def main():
    """Main function of the module"""
    config = configparser.ConfigParser()
    dir = os.path.dirname(os.path.abspath(__file__))
    config.read(dir + os.sep + 'config.ini')

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config['default']['host']))
    channel = connection.channel()
    channel.queue_declare(queue=config['default']['queue_name'])

    while True:
        result = channel.basic_get(queue=config['default']['queue_name'], auto_ack=True)
        if result[2] is not None:
            logger.info("Message Received: " + str(result[2]))
        else:
            logger.info("Waiting for messages. To exit press CTRL+C")
            connection.sleep(int(config['default']['timer']))

if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Creating new log file")
    logger.info("Logging setup completed")
    main()
