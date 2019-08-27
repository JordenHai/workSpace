import threading
import time


def run(n):
    print("task %s--->"%n)
    lock.acquire()
    global num
    num = num + 1
    lock.release()


    pass

lock = threading.Lock()


num = 0
thread_obj = []
for i in range(100):
    t = threading.Thread(target=run,args=('t_%s'%i,))
    # t.setDaemon(True)
    t.start()

    thread_obj.append(t)

for res in thread_obj:
    res.join()

print("-----Main Thread------")

print("num",num)