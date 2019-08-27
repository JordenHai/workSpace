import pika
import uuid
import time


class FibonacciRpcClient(object):
    def __init__(self):
        # credentials = pika.PlainCredentials('alex','alex3714')
        #
        # self.connection = pika.BlockingConnection(pika.ConnectionParameters(
        #                     host='10.20.224.10',virtual_host='/',credentials=credentials))
        #
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='',exclusive=True)
        self.callback_queue = result.method.queue

        #接收的路径
        self.channel.basic_consume(queue = self.callback_queue,
                                   on_message_callback=self.on_response,
                                   auto_ack=True)

    def on_response(self,ch,method,property,boby):
        if self.corr_id == property.correlation_id:
            self.response = boby
        pass
    
    def call(self,res):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        # 发送的路径在routing_key
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,),
                                    body = res)
        
        self.channel.basic_ack(delivery_tag=method.delivery_tag)
        while self.response is None:
            self.connection.process_data_events()
        return self.response



if __name__ == "__main__":

    fibonacci = FibonacciRpcClient()
    print("[x]...................[x]")
    res = input(">>")
    data = fibonacci.call(res)
    response = str(data,'utf-8')
    print(response)

