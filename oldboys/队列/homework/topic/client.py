import pika

class Client():
    
    def __init__(self,host,severity=[],exchange='',exchange_type=''):
        self.host = host
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.severity = severity
        self.queue_name = None
        self.connection = pika.BlockingConnection(
                                pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.__exchange()
        self.__queue()
        self.__queue_bind()

    def __exchange(self):
        # for res in self.exchange:
        #     self.channel.exchange_declare(exchange=res,
        #                             exchange_type=self.exchange_type)
        self.channel.exchange_declare(exchange=self.exchange,
                                    exchange_type=self.exchange_type)
        pass

    def __queue(self):
        # for res in self.exchange:
        result = self.channel.queue_declare(queue='',
                                            exclusive=True)
        val = result.method.queue
        self.queue_name = val
        pass

    def __queue_bind(self):
        for res in self.severity:
            self.channel.queue_bind(queue=self.queue_name,
                                    exchange=self.exchange,
                                    routing_key=res)
        pass

    def __publish(self):
        self.channel.basic_publish(exchange=self.exchange,
                                    routing_key = self.severity,
                                    body = self.response)
        pass
    def __consume(self):
        self.channel.basic_consume(queue=self.queue_name,
                                    on_message_callback=self.__response,
                                    auto_ack=True)
        pass
    def __response(self,ch,method,properties,body):
        print(" [x] %r:%r" % (method.routing_key,body))
        pass
    
    def call(self):
        self.channel.basic_qos(prefetch_count=2)
        self.__consume()
        pass

    def start_consume(self):
        self.channel.start_consuming()

if __name__ == "__main__":
    c = Client(host = 'localhost',
                severity=['*.info','*.erro'],
                exchange='topic_',
                exchange_type='topic')
    c.call()
    c.start_consume()