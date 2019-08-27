import pika

class Client():
    def __init__(self,host):
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=self.host))
 
        self.channel = self.connection.channel()
 
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
 
        self.channel.basic_consume(self.__response, no_ack=True,
                                   queue=self.callback_queue)
        pass
    
    def __response(self,ch,method,property,body):
        pass
    
    def func(self):
        pass
    
    def call(self):

        pass
