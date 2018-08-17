
import unittest
import json
import re


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FcO')


if __name__=='__main__':
    # result =  "bitcoincash:qr30v9s0l99zgfq802wkjsgylwx4l9aeush2yvvpye"
    # result = result[12:]
    # print(result)
    # reobj = re.match('^0x[a-fA-F0-9]{40}','0xeweioiqox12333')
    # result = {"valid_address": True} if reobj else {"valid_address": False}

    # r = "\"JSONDecodeError('Expecting value: line 1 column 1 (char 0)',)\""
    # r = r[:r.find('(')]
    # r = r[r.find("\"")+1:]
    # print(r)
    unittest.main()