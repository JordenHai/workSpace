
import multiprocessing
import os

def info(title):
    print(title)
    print("module name:",__name__)
    print('parent process:',os.getppid())
    print("process id：",os.getpid())
    print("\n\n")

def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello',name)

if __name__ == "__main__":
    info("\033[32;1mmain process line\033[0m")
    p = multiprocessing.Process(target=f,args=('bob',))
    p.start()
    p.join()

# 子进程都是由父进程 调用生成的