
import redis

# r = redis.Redis(host='192.168.235.131',port=6379)
#
# r.set('foo','bar')
# print(r.get('foo'))

pool = redis.ConnectionPool(host='192.168.235.131',port=6379)

r = redis.Redis(connection_pool=pool)

r.set('f','g')
print(r.get('f'))

