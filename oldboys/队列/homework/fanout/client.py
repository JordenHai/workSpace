import pika

class Client():
    
    def __init__(self,host,exchange='',exchangeType='fanout'):
        
        self.host = host
        
        self.exchange = exchange
        
        self.exchangeType = exchangeType

        self.connection = pika.BlockingConnection(
                                pika.ConnectionParameters(host=self.host))
        
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange=self.exchange,
                                       exchange_type = exchangeType)
        result = self.channel.queue_declare(queue='',
                                             exclusive = True)
        self.queue_name = result.method.queue

        self.channel.queue_bind(queue=self.queue_name,
                                 exchange=self.exchange)
        
        self.channel.basic_consume(queue = self.queue_name,
                                    on_message_callback = self.on_response,
                                    auto_ack = True)
    def call(self):
        self.response = None
        
        while self.response is None:
            self.connection.process_data_events()
        print(self.response)
    
    def on_response(self,ch,method,property,body):
        self.response = body
        pass

if __name__ == "__main__":
    c = Client(host='localhost',exchange='logs')
    while True:
        c.call()
    pass