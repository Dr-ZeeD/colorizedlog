# -*- coding: utf-8 -*-
import logging


__version__ = '0.1.0'


DEFAULT = '\x1b[0m'

BLACK_FG = '\x1b[30m'
RED_FG = '\x1b[31m'
GREEN_FG = '\x1b[32m'
YELLOW_FG = '\x1b[33m'
BLUE_FG = '\x1b[34m'
MAGENTA_FG = '\x1b[35m'
CYAN_FG = '\x1b[36m'
WHITE_FG = '\x1b[37m'
DEFAULT_FG = '\x1b[39m'

BLACK_BG = '\x1b[40m'
RED_BG = '\x1b[41m'
GREEN_BG = '\x1b[42m'
YELLOW_BG = '\x1b[43m'
BLUE_BG = '\x1b[44m'
MAGENTA_BG = '\x1b[45m'
CYAN_BG = '\x1b[46m'
WHITE_BG = '\x1b[47m'
DEFAULT_BG = '\x1b[49m'


class ColorStreamHandler(logging.StreamHandler):

    def __init__(self, stream=None):
        super(ColorStreamHandler, self).__init__(stream)

    @staticmethod
    def _get_color(level):
        if level >= logging.CRITICAL:
            return MAGENTA_FG
        elif level >= logging.ERROR:
            return RED_FG
        elif level >= logging.WARNING:
            return YELLOW_FG
        elif level >= logging.INFO:
            return GREEN_FG
        elif level >= logging.DEBUG:
            return CYAN_FG
        else:
            return DEFAULT

    def format(self, record):
        text = super(ColorStreamHandler, self).format(record)
        color = self._get_color(record.levelno)
        return color + text + DEFAULT
