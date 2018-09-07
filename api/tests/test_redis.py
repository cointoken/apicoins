import redis

rs = redis.Redis(host='192.168.1.151',port=6379)
# print(r.rpush("1",2))
# print(r.rpush("1",3))
# print(r.rpush("1",4))
# print(r.rpush("1",5))
# print(r.rpush("1",6))
# print(r.rpush("1",7))

# print(rs.blpop("1"))
# print(rs.blpop("1"))
# print(rs.blpop("1"))
# print(rs.blpop("1"))
# print(rs.blpop("1"))
# print(rs.blpop("1"))

# if rs.llen("1")==0：
#     for i in range(0,8):
#         print()

print(rs.llen("eth"))
rs_len = rs.llen("eth")
if rs_len==0: 
    rs.rpush("eth","0x098A05Cc69f7D883C109e777F3380E5922F778E5")
    rs.rpush("eth","0x6094589988a9563D6cA3420DA3B8B663965337f4")
else:
    print(bytes.decode(rs.lpop("eth")))
    # if rs.lpop("eth")==3:
    #     print(1)
    # for i in range(0,rs_len):
    #     print(rs.lpop("eth"))