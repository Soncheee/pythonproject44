import json
from idlelib.iomenu import encoding
from json import JSONDecodeError
import logging


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('../logs/example.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG,


                    filemode='w')

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')


def connect_json(path_file):
    try:
        with open(path_file, 'r', encoding='utf-8') as file:
            print('hi')
    except FileNotFoundError as f:
        print(f.__class__.__name__)
        return []
    except JSONDecodeError as j:
        print(j.__class__.__name__)
        return []

connect_json()
