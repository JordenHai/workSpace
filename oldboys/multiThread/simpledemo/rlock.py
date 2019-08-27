import threading

def run1():
    lock.acquire()
    global num
    num = num + 1
    lock.release()
    pass


def run2():
    lock.acquire()
    global num2
    num2 = num2 + 1
    lock.release()
    pass

def run3():
    lock.acquire()
    run1()
    print("-------- Do something --------")
    run2()
    lock.release()
    pass

num,num2 = 0,0
lock = threading.RLock()
t_obj = []
for i in range(12):
    t = threading.Thread(target=run3)

    t.start()

    t_obj.append(t)

for res in t_obj:
    res.join()

while threading.active_count() != 1:
    print(threading.activeCount())

else:
    print("--------Main Threading--------")
    print(num,num2)

# 锁的钥匙被弄混了
locks = {
    "door1":"key1",
    "door2":"key2",
}

# 锁 就是互斥 锁
# Mutex 