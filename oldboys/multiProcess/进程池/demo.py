from multiprocessing import Pool,freeze_support,Process
import time,os

def Foo(i):
    time.sleep(1.2)
    print('in the process :',os.getpid())
    return i+100

def Bar(arg):
    print('-->exec done:',arg)
    print("Bar's PID",os.getpid())


# 把其当做脚本是执行下程序 当做模块导入时，下面的语句并不会执行
if __name__ == '__main__':
    # freeze_support()
    # 挂起五进程
    pool = Pool(processes=5)  #允许进程池 同时放入 五个 进程
    print('Main Process PID',os.getpid())
    for i in range(10):
        # 并行执行
        pool.apply_async(func=Foo,args=(i,),callback=Bar)#callback 回调 执行完前一个 在执行下一个
        # pool.apply(func=Foo,args=(i,))#串行执行
        # pool.apply_async(func=Foo,args=(i,))
    print('end')
    pool.close()
    pool.join()

    # 等其关闭之后 在 join()
    # 没有join  直接关闭程序