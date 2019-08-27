import socketserver

class MyTCPHandle(socketserver.BaseRequestHandler):
    '''
    The request handler class
    '''
    def handle(self):
        while True:
            try:
                #self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()

                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                # if not self.data:#客户机断开了
                #     print(self.client_address[0],"break the connetion")
                #     break
                #just send back the same data but upper-cased
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break
        pass

if __name__ == "__main__":
    HOST,PORT = "localhost",9997
    #Create the server ,binding to localhost on port
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandle)
    server.serve_forever()

    pass
