
import pika
import json
import threading
import os
class RpcServer:

    def __init__(self):
        credentials = pika.PlainCredentials('alex', 'alex3714')
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',))

        self.channel = self.conn.channel()

        result = self.channel.queue_declare(queue='rpc_queue')
        self.queue = result.method.queue


    def execfunction(self,command):
        res = "test"
        return res
        pass

    def check(self,*args):
        props_id = args[0].correlation_id

        pass

    def on_request(self,ch,method,property,body):
        command = str(body,'utf-8')
        print(">>:%s"%command)
        com = command.split(' ')[0]
        print(com)
        # if hasattr(self,command):
        #     func = getattr(self,command)
        #     func(property,body)
        # else:
        self.response = self.execfunction(command)

        ch.basic_publish(exchange='',
                        routing_key = property.reply_to,
                        properties=pika.BasicProperties(
                                    correlation_id= property.correlation_id),
                        body = self.response)

        self.channel.basic_ack(delivery_tag=method.delivery_tag)

    def call(self):
        self.channel.basic_qos(prefetch_count=2)
        self.channel.basic_consume(queue=self.queue,
                                   on_message_callback=self.on_request,
                                   auto_ack=False)
        pass
    def start_consume(self):
        self.channel.start_consuming()


if __name__ == "__main__":
    r = RpcServer()
    r.call()
    r.start_consume()    
    pass