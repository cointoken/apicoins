
import unittest
import json

datas = {
    "data": {
        "info": [
            {
                "abandoned": False,
                "account": "",
                "address": "1KHBHjNDxRFoTw125j6kBHhXdThUnaZAK3",
                "amount": "0.04890000",
                "bip125-replaceable": "no",
                "blockhash": "000000000000000000308e1a8dc55951337ffd1b5b027847d00e18196c0214ed",
                "blockindex": 135,
                "blocktime": 1528695642,
                "category": "send",
                "confirmations": 7554,
                "fee": "0.00016800",
                "time": 1528694277,
                "timereceived": 1528694277,
                "txid": "94ffc790c382897356e5064dbc79582bbf3189aef99e14a63b3c72b04caca620",
                "vout": 0,
                "walletconflicts": []
            },
            {
                "abandoned": False,
                "account": "",
                "address": "2KHBHjNDxRFoTw125j6kBHhXdThUnaZAK3",
                "amount": "0.04890000",
                "bip125-replaceable": "no",
                "blockhash": "000000000000000000308e1a8dc55951337ffd1b5b027847d00e18196c0214ed",
                "blockindex": 135,
                "blocktime": 1528695642,
                "category": "send",
                "confirmations": 7554,
                "fee": "0.00016800",
                "time": 1528694277,
                "timereceived": 1528694277,
                "txid": "94ffc790c382897356e5064dbc79582bbf3189aef99e14a63b3c72b04caca620",
                "vout": 0,
                "walletconflicts": []
            },
            {
                "abandoned": False,
                "account": "",
                "address": "3KHBHjNDxRFoTw125j6kBHhXdThUnaZAK3",
                "amount": "0.04890000",
                "bip125-replaceable": "no",
                "blockhash": "000000000000000000308e1a8dc55951337ffd1b5b027847d00e18196c0214ed",
                "blockindex": 135,
                "blocktime": 1528695642,
                "category": "send",
                "confirmations": 7554,
                "fee": "0.00016800",
                "time": 1528694277,
                "timereceived": 1528694277,
                "txid": "94ffc790c382897356e5064dbc79582bbf3189aef99e14a63b3c72b04caca620",
                "vout": 0,
                "walletconflicts": []
            }
        ]
    },
    "message": "success",
    "status": 200
}


if __name__=='__main__':
   # js = json.loads(datas)
    js = datas['data']['info']
    for j in js:
        #print(current_second_time-j['time'])
