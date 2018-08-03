import sys
import logging
log_format = ' '.join([
    '[%(asctime)s]',
    '[%(process)d-%(thread)d]',
    '%(levelname)s',
    '-',
    '%(message)s'
])


def get_logger():
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format=log_format)
    return logging
