#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

# https://pypi.org/project/redis/

import redis
import json

class Order(object):
     def __init__(self, price: int, count: int, isin: str) -> None:
          self.price = price
          self.count = count
          self.isin  = isin
          pass
     def to_dict(self) -> dict:
          return {
               'price' : self.price,
               'count' : self.count,
               'isin'  : self.isin,
          }

class RedisWrapper(object):
     def __init__(self) -> None:
          self.pool = redis.ConnectionPool(host= '172.16.51.115', port= 6379, db= 0)
          self.connection = redis.Redis(connection_pool= self.pool, decode_responses= True)
          self.channel = 'orders'
          pass
     
     def send(self, data: dict) -> None:
          self.connection.publish(self.channel, json.dumps(data))

     def recv(self) -> dict:
          p = self.connection.pubsub()
          p.subscribe(self.channel)
          return p.get_message()
          
order = Order(10, 50, 'IRO1BAMA0001')
rwrap = RedisWrapper()
rwrap.send(order.to_dict())
x = rwrap.recv()
print(x)
