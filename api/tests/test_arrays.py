import unittest
from datetime import datetime,timedelta


def now_time(hours):
    return (datetime.now()-timedelta(hours=hours)).strftime('%Y-%m-%d')

if __name__=='__main__':
    print(now_time(8))
    print(now_time(0))