import threading
import time

def run(n):
    print("task:",n)
    time.sleep(2)
    print("task-end",n)


# t1 = threading.Thread(target=run,args=('t1',))
# t2 = threading.Thread(target=run,args=('t2',))
# t1.start()
# t2.start()
thread_list = []
start_time = time.time()
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()
    #为了不阻塞后面的线程的启动 不再此处join 放到列表中
    thread_list.append(t)

# for res in thread_list:
#     # print(threading.active_count())
#     res.join()

print("-------ALL Threads Has been Finished--------",threading.current_thread())
time.sleep(1.9)
end_time = time.time()

print("cost",end_time-start_time)

# 主线程 启动了 子线程之后 子线程与主线程是并行的关系
