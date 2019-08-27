import pika

# 利用direct模式 重新写 这周

# #建立连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
# #生成通道
# channel = connection.channel()

class Server():
    def __init__(self,host,exchange='',exchangeType='fanout'):
        self.host = host
        self.exchange = exchange
        self.exchangeType = exchangeType
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange,
                                      exchange_type =self.exchangeType)
    def call(self):
        
        msg = input(">>").strip()
        self.message = msg
        self.channel.basic_qos(prefetch_count=2)
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key = '',
                                   body = self.message)
        pass


if __name__ == "__main__":
    s = Server(host='localhost',exchange='logs')
    while True:
        s.call()
    pass
        