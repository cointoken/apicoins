import unittest
from datetime import datetime,timedelta
from coins.btc import Btc
from coins.eth import Eth

def now_time(hours):
    return (datetime.now()-timedelta(hours=hours)).strftime('%Y-%m-%d')

def test_btc():
    btc = Btc(8332,'apx','DEOXMEIO943JKDJFIE3312DFKIEOK')
    btc_accounts = btc.listaccounts()
    for key,value in btc_accounts.items():
        amount = btc_accounts[key]
        print(amount)

if __name__=='__main__':
    print(now_time(48))
    print(now_time(0))