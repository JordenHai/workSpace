
import pika
import sys, os
import time
import uuid


class RpcServer(object):
    def __init__(self):
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.conn.channel()

    def fib(self, n):  # 定义一个主逻辑:斐波那契数列.===>程序的处理逻辑在这里写.
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def on_request(self, channel, method, properties, body):
        print('----------------------------------------')
        print('正在消费的消息:====>%s' % body)
        time.sleep(5)
        print('消息的相关属性为:')
        print(properties)
        value = self.fib(int(body))
        print('原值: ', body, '斐波那契的运行结果: ', value)

        print('将计算的运行结果返回给RPC客户端....')
        self.channel.basic_publish(exchange='',
                                   routing_key=properties.reply_to,
                                   body=str(value),
                                   properties=pika.BasicProperties(
                                       # delivery_mode=2,
                                       correlation_id=properties.correlation_id,
                                   ))

        self.channel.basic_ack(delivery_tag=method.delivery_tag)
        print('----------------------------------------')

    def call_back(self):
        self.channel.basic_qos(prefetch_count=2)
        self.channel.basic_consume(consumer_callback=self.on_request,
                                   queue='rpc_queue',
                                   no_ack=False)

    def start_consume(self):
        self.channel.start_consuming()


if __name__ == '__main__':
    fibonaci = RpcServer()
    fibonaci.call_back()
    fibonaci.start_consume()
