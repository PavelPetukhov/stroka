import logging


# Custom formatter
class LogFormatter(logging.Formatter):

    err_fmt = '%(asctime)s %(name)s %(levelname)s %(module)s : line  %(lineno)d : %(message)s'
    dflt_fmt = '%(asctime)s %(name)s %(levelname)s %(message)s'

    def __init__(self):
        super().__init__(fmt=LogFormatter.dflt_fmt, datefmt=None, style='%')

    def format(self, record):
        format_orig = self._style._fmt
        if record.levelno == logging.ERROR:
            self._style._fmt = LogFormatter.err_fmt

        result = logging.Formatter.format(self, record)
        self._style._fmt = format_orig
        return result
