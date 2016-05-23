import logging

LEVELS = {
    2: logging.DEBUG,
    1: logging.INFO,
    0: logging.ERROR,
}


def set_logger(verbosity):
    level = LEVELS.get(verbosity, logging.WARNING)
    logging.basicConfig(level=level)
