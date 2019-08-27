from gevent import monkey
from urllib import request
import gevent,time
monkey.patch_all()
# 把当前程序的所有IO操作给我单独坐上标记
def f(url):
    print('GET:%s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    str = url.split('/')[-2].split('.')[-2] + '.html'
    f = open(str,'wb')
    f.write(data)
    f.close()
    print('%d from %s.'%(len(data),url))

urls = [
    'https://www.python.org/',
    'https://www.yahoo.com/',
    'https://github.com/',
    ]

# url = urls[1]
# strs = url.split('/')
# str = strs[-2].split('.')
# print(str[-2])


t1 = time.time()
gevent.joinall([
    gevent.spawn(f, urls[0]),
    gevent.spawn(f, urls[1]),
    gevent.spawn(f, urls[2]),
])
t2 = time.time()

# 如果没有将monkey导入 gevent不知道进行了IO操作

for url in urls:
    f(url)

t3 = time.time()

print(t2 - t1)
print(t3 - t2)