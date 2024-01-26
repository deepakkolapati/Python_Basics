import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

filehandler=logging.FileHandler("book.log")
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

