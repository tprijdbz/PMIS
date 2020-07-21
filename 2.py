from redis import *

r = StrictRedis(host = '127.0.0.1', port= 6379)

#r.set('name', 'kingname')
print(r.get('name'))
print(r.get('name'))
#r.append('name', ' is a super man. ')
print(r.get('name'))
print(r.keys())
r.delete('name')
print(r.keys())

