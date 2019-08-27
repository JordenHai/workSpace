# 仅仅 是 数据传递
from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42, 'hello from child'])
    conn.send([43, 'hello from child'])
    print("from parent:",conn.recv())
    conn.close()
    pass

if __name__ == '__main__':
    parent,child = Pipe()
    p = Process(target=f,args=(child,))
    p.start()
    print(parent.recv())
    print(parent.recv())
    parent.send('is ok')

    p.join()