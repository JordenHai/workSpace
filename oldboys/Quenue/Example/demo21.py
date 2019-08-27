import queue
# import threading
#
#
# def run():
#     lock.acquire()
#     if not q.empty():
#         print(q.get())
#     else:
#         q.put(5)
#     lock.release()
#     pass
#
# def run2():
#     lock.acquire()
#     if not q.empty():
#         print(q.get())
#     else:
#         q.put(4)
#     lock.release()
#
# l = threading.Thread(target=run,)
# l1 = threading.Thread(target=run2,)
# lock = threading.RLock()
# q = queue.Queue(1)
# l1.start()
# l.start()
#
# # q.empty()
# # 判断q是否为空

queuePriority = queue.PriorityQueue()
queuePriority.put((10,"alex"))
queuePriority.put((25,"han"))
queuePriority.put((30,"jiaohai"))

print(queuePriority.get())
print(queuePriority.get())
print(queuePriority.get())
