import json
import requests
import collections


data = "{\"status\":200,\"message\":\"success\", \"data\":{\"deposits\":[{\"fund_uid\":\"\",\"amount\":10000,\"currency\":\"btc\"},{\"fund_uid\":\"\",\"amount\":8888,\"currency\":\"ltc\"}] }}"


def test_getdata():
    url = 'http://47.75.91.163:8080/api/v1/getnewaddress/ltc'
    r = requests.get(url)
    j = json.loads(r.content)
    if isinstance(j,str):
        print(j)
    elif isinstance(j,dict):
        print('dict')
    print(j['data'])
    dic = {}
    dic['cc'] = 'ccc'
    dic['dd'] = 'ddd'
    dic['ee'] = 'ee'
    for key,value in dic.items():
        print(dic[key])   
    
def test_data():
    j = json.loads(data)
    if isinstance(j,str):
        print('str')
    elif isinstance(j,dict):
        print('dict')
    arrs = j['data']['deposits']
    for a in arrs:
        print(a['currency'])

if __name__ == '__main__':
    test_data()