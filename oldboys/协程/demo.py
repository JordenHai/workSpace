# 协程 -- 微线程 coroutine 协程是一种用户态的轻量级线程
# 协程能保留上一次调用的状态 每次过程重入时，就相当于进入 上一次 调用的状态
# 换种说法 就是进入上一次离开时所处的逻辑流的位置

# 无需 线程 上下文的切换的开销
# 无需 原子操作锁定及同步的开销 改一个变量的操作 就是原子操作
# 方便切换控制流 简化编程模型
# 高并发 高扩展 低成本
# 一个CPU支持上万个协程都是不是问题
# 适合高并发处理

# 协程需要和进程配合才可以实现多核利用
import time
def consumer(name):
    print("-------------->")
    while True:
        baozi = yield
        print('[%s] --[%s]'%(name,baozi))

# prodecer 能够获取到 con 和con2 说明其是在一个线程中资源是处于共享状态
# 说明协程 是一个线程

def producer():
    r = con.__next__()
    r1 = con2.__next__()
    n = 0
    while n<25:
        n += 1
        con.send(n)
        con2.send(n)
        time.sleep(0.5)
        print('[prodecer] [baozi] %s'%n)

if __name__ == '__main__':
    con = consumer('kk')
    con2 = consumer('dd')
    p = producer()
