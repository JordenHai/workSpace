
# 异步爬虫
# 游戏开发
# 服务器端开发
# select 必须要处于非阻塞模式
import select
import socket
import sys
import queue
msg = {}
inputs = []
outputs = []

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.setblocking(False)

address = ('localhost',9000)

server.bind(address)

server.listen(1000)

inputs.append(server)
while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    print(readable,writeable,exceptional)

    for res in readable:
       if res is server:
           conn,addr = server.accept()
           print('new connection')
           conn.setblocking(0)
           inputs.append(conn)
           msg[conn] = queue.Queue()  #初始化一个队列，存返回给客户端的数据
       else:
           data = res.recv(1024)
           if data:
               print("收到来自[%s]的数据:" % res.getpeername()[0], data)
               msg[res].put(data)
               if res not in outputs:
                    outputs.append(res) #放入返回的链接队列中
           else:
               print('客户端断开连接',res)
               if res in outputs:
                   outputs.remove(res)

               inputs.remove(res)

               del msg[res]

    for w in writeable:#要返回给客户端的链接列表
        try:
            data = msg[w].get_nowait()
        except queue.Empty:
            outputs.remove(w)#确保下次链接 不返回这个已经返回的数据
        else:
            print("sending msg to [%s]"%w.getpeername()[0], data)
            w.send(data)

    for e in exceptional:
        inputs.remove(e)
        if e in outputs:
            outputs.remove(e)

        del msg[e]
        e.close()
        pass