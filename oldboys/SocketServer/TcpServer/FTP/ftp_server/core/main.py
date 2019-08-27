import socketserver
import json
import os
class MyTcpServer(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionResetError as e:
                print("err",e)
                break

    def put(self,*args):
        cmd_dict = args[0]
        filename = cmd_dict["filename"]
        size = cmd_dict["size"]
        if os.path.isfile(filename):
            f = open(filename+".new","wb")
        else:
            f = open(filename,"wb")

        self.request.send(b"200,OK")

        received_size = 0
        while received_size < size:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file[%s] has uploaded..."%filename)

    def get(self,*args):
        pass

if __name__ == "__main__":
    HOST,PORT = "localhost",9997
    #Create the server ,binding to localhost on port
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTcpServer)
    server.serve_forever()

    pass
