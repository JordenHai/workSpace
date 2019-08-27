import threading
import time
def run(n):
    semaphore.acquire()
    print("Run the thread :%s\n"%n)
    time.sleep(1.5)
    semaphore.release()
    pass



if __name__ == '__main__':
    num = 0
    t_obj = []
    semaphore = threading.BoundedSemaphore(5)
    for i in range(22):
        t = threading.Thread(target=run,args=(i,))
        t.start()
        t_obj.append(t)

    for res in t_obj:
        res.join()

while threading.active_count() != 1:
    pass

else:
    print("--------------------")