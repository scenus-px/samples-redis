#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

# https://pypi.org/project/redis/

import redis

pool = redis.ConnectionPool(host= '172.16.51.115', port= 6379, db= 0)
r = redis.Redis(connection_pool=pool, decode_responses= True)

pipe = r.pipeline()
print(pipe.set('foo', 5))
print(pipe.set('bar', 18.5))
print(pipe.set('blee', "hello world!"))
x = pipe.execute()

print(x)