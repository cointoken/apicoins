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
    for i in range(0,8):
        rs.rpush("eth","cddd"+str(i))
else:
    print(str(rs.lpop("eth")))
    # if rs.lpop("eth")==3:
    #     print(1)
    # for i in range(0,rs_len):
    #     print(rs.lpop("eth"))