import time

class Util(object):
    @classmethod
    def get_curr_seconds(cls):
        return int(round(time.time()))