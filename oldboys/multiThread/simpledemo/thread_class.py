import threading
import time

class myThread(threading.Thread):

    def __init__(self,n,sleep_time):
        super(myThread,self).__init__()
        self.n = n
        self.sleep_time = sleep_time
    def run(self):
        print("running %s's task"%self.n)
        time.sleep(self.sleep_time)
        print("task %s's has been done"%self.n)
    pass

start_time = time.time()
t1 = myThread('12',2)
t2 = myThread('22',4)
t1.start()
t2.start()
t1.join()#wait()
end_time = time.time()
print("finish time of the t1:",end_time-start_time)
t2.join()#wait()
end_time = time.time()
print("finish time of the t2",end_time-start_time)
print("main thread---------")
