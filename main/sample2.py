#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

# https://pypi.org/project/redis/

import redis

pool = redis.ConnectionPool(host= '172.16.51.115', port= 6379, db= 0)
r = redis.Redis(connection_pool=pool, decode_responses= True)

p = r.pubsub()
p.subscribe('my-first-channel', 'my-second-channel')
x = p.get_message()
print(x)

