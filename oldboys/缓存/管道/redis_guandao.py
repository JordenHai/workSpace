import redis
import time
pool = redis.ConnectionPool(host='192.168.235.131',port=6379,db=5)

r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

# r.set('f','g')
# time.sleep(5)
# r.set('role','sb')

# r.brpoplpush('names','names2',timeout=30)

pipe.set('name','alex')
time.sleep(5)
pipe.set('role','sb')

pipe.execute()