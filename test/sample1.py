#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

# https://pypi.org/project/redis/

import redis

r = redis.Redis(host= '172.16.51.115', port= 6379, db= 0, decode_responses= True)
b = r.set('foo', 'bar')
print(b)
print(r.get('foo'))

