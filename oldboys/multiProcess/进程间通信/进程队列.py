# 进程Queue 和 线程的 queue 是不同的
#
# 进程Queue是用pickle进行序列化的
#
# 进程之间 资源不共享
#
# 线程之间 资源共享 子进程 访问不了 父进程的数据
#

# 仅仅只是数据的传递
from multiprocessing import Process,Queue

def f(q):
    q.put([42,None,'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()

    print(q.get())

    p.join()
#这使得我们感觉 我们共享了一份资源
# 其实是克隆了一份资源 进行共享
# 队列的数据 被 pickle了 使其序列化
# 传到了一个中间位置
# 中间位置 通过反序列化 到另一个队列

# import threading
# import queue
#
# def f():
#     q.put('dd')
#
# if __name__ == "__main__":
#     q = queue.Queue()
#     p = threading.Thread(target=f,)
#     p.start()
#
#     print(q.get())
#     p.join()