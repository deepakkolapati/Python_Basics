import logging

def get_logger():
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter=logging.Formatter('%(asctime)s:%(filename)s:%(lineno)s:%(levelname)s:%(message)s')

    filehandler=logging.FileHandler("book.log")
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)
    return logger