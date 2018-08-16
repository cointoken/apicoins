import json
import requests
import collections

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
    


if __name__ == '__main__':
    test_getdata()