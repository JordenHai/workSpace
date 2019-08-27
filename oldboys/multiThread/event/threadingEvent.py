'''

    event.wait()
    event.set()
    event.clear()

    if  the flag is set the wait method doesn't do anything
    标志位设定了 代表放行

    if the flag is cleared ，wait  will block until it becames set again
    标志位被清空 代表阻塞 wait 等待放行

    Any number of threads may wait for the same event
'''

import threading
import time

event = threading.Event()

def light():
    count = 0
    event.set()
    while True:
        if count > 10 and count < 30:#改成红灯
            event.clear()

            print("\033[41;1m red light is on ...\033[0m")
        elif count > 30:#过十秒
            event.set()

            count = 0
        else:
            print("\033[1;30;42m green light is on ...\033[0m")

        time.sleep(0.1)
        count +=1


def car(name):
    while True:
        if event.is_set():#代表绿灯
            print("[%s] running---> "%name)
            time.sleep(0.2)
        else:
            print("[%s] see the red light"%name)
            event.wait()
            print("\033[34;1mThe light turns to the green\033[0m")

event = threading.Event()


l = threading.Thread(target=light,)
l.start()

car1 = threading.Thread(target=car,args=('tesla',))
car1.start()