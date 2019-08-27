
from gevent import monkey
import gevent
import socket
monkey.patch_all()

def server(port):
    s = socket.socket()

    s.bind(('0.0.0.0',port))
    s.listen(500)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handle_request,cli)

def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print('recv:',data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
    pass

if __name__ == '__main__':
    server(8000)