import logging

def __init__(self,app):
    logging.basicConfig(level=logging.error,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt = '%a,%d %b %Y %H:%M:%S',
                        filename = 'logs/errors.log',
                        filemode = 'a+')
    self.app = app


