import gevent

# gevent中的主要模式是Greenlet
# 以C扩展的模块形式接入到Python的轻量级协程
# 全部运行在操作系统进程的内部 但他们被协作式的调度

def Foo():
    print('running in foo')
    gevent.sleep(1)
    # 模仿IO操作
    print('Explicit context switch back to foo ')

def Bar():
    print('Explicit context to bar')
    # Explicit精确的
    gevent.sleep(2)
    print("Implicit context switch back to bar")

def Strs():
    print('Explicit context to Strs')
    gevent.sleep(1.5)
    print("Implicit context switch back to Strs")

gevent.joinall([
    gevent.spawn(Foo),#产生 发起 spawn
    gevent.spawn(Bar),
    gevent.spawn(Strs),
])
