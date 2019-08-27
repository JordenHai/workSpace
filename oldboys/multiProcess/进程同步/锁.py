from multiprocessing import Process,Lock
# 控制 屏幕打印
def f(l,num):
    l.acquire()
    try:
        print('hello world',num)
    finally:
        l.release()

    pass

if __name__ == '__main__':
    lock = Lock()

    for res in range(100):
        Process(target=f,args=(lock,res)).start()

