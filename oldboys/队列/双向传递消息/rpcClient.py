import pika
import uuid
import time

class RpcClient(object):
    def __init__(self,client):
        self.host = client
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
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
    
    def call(self,command):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        # 发送的路径在routing_key
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,),
                                    body = command)

        while self.response is None:
            self.connection.process_data_events()
            #非阻塞版的start_consuming()
            print('no msg....')
            time.sleep(0.5)
        return self.response
    
fibonacci = RpcClient('localhost')
print("[x]...................[x]")

# 1 1 2 3 5 8 13 21 34
# 1 2 3 4 5 6 7  8  9

response = fibonacci.call('ifconfig')

print(response)

