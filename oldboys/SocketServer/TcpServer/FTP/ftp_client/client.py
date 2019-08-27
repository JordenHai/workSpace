import socket
import os
import json
class Ftpclient(object):

    def __init__(self):
        self.client = socket.socket()
        pass

    def help(self):
        msg = '''
            ls
            pwd
            cd ../..
            get filename
            put filename
            
            '''

    def connet(self,ip,port):
        self.client.connect((ip,port))
        pass

    def interactive(self):
        # self.authenticate()
        while True:
            cmd = input(">>").strip()
            if len(cmd) ==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s"%cmd_str):
                func = getattr(self,"cmd_%s"%cmd_str)
                func(cmd)
            else:
                self.help()
        pass

    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                #标准化文件
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "size":filesize,
                    "overridden":True
                }

                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                print(json.dumps(msg_dic))
                #防止粘包，等待确认
                server_response = self.client.recv(1024).decode("utf-8")
                #处理确认包
                f = open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload finished")
                    f.close()
            else:
                print(filename,"is invailad")
        pass

    def cmd_get(self):
        pass

ftp = Ftpclient()
ftp.connet("localhost",9997)
ftp.interactive()