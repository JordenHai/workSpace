import threading,time
import queue,random

q = queue.Queue(maxsize=10)
#
# def producer(name):
#     count = 0
#     remain = 0
#     while True:
#         if event.is_set():
#             print("开始做饭")
#
#             for i in range(10 - q.qsize()):
#                 q.put("骨头%s"%count)
#                 count = count + 1
#                 if i == int(10 - random.random()*10):
#                     break
#             print("remain：%s"%q.qsize())
#             event.clear()
#         else:
#             event.wait()
#
# def cusumer(name):
#     num = 0
#     while True:
#         while q.qsize() > 0:
#             num = num + 1
#
#             print("%s 取到 %s 吃掉它,总共吃了%s"%(name,q.get(),num))
#
#             event.clear()
#             time.sleep(0.2)
#         else:
#             event.set()
#
#
# event = threading.Event()
#
#
# p = threading.Thread(target=producer,args=('Alex',))
#
# c = threading.Thread(target=cusumer,args=('a',))
# c1 = threading.Thread(target=cusumer,args=('b',))
# c2 = threading.Thread(target=cusumer,args=('c',))
#
# q.put("")
#
# p.start()
# c.start()
# c1.start()
# c2.start()
#
#

def product(name):

    count = 1
    while True:
        q.put("gutou%s"%count)
        # print("CountNum%s"%count)
        count +=1
        time.sleep(0.11)

def consume(name):

    while True:
        if q.qsize() > 0:
            print("%s eat %s"%(name,q.get()))

t = threading.Thread(target=product,args=('alex',))
c2 = threading.Thread(target=consume,args=('a',))
c1 = threading.Thread(target=consume, args=('b',))
c3 = threading.Thread(target=consume, args=('c',))

t.start()
c1.start()
c2.start()
c3.start()
