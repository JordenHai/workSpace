import pika

class Server():
    
    def __init__(self,host,exchange='',exchange_type=''):
        self.host = host
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.severity = None
        self.connection = pika.BlockingConnection(
                                pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.__exchange()
        
    def __exchange(self):

        self.channel.exchange_declare(exchange=self.exchange,
                                        exchange_type=self.exchange_type)
        pass

    def __publish(self):
        self.channel.basic_publish(exchange=self.exchange,
                                    routing_key = self.severity,
                                    body = self.response)
        pass
    def call(self,msg,response):
        self.response = response
        self.severity = msg
        self.__publish()
        pass


if __name__ == "__main__":
    s = Server(host='localhost',exchange='direct_',exchange_type='direct')
    while True:
        msg = input(">>:").split(' ')
        s.call(msg[0],msg[1])
    pass

