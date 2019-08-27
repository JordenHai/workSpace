# 没有声明queue是因为这是广播消息 不需要队列
#其实就是订阅模式
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# 转发器声明
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# message = ''.join(sys.argv[1:]) or 'info:hello world'
message = 'hello world'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print("[x] sent %r "%message)
connection.close()
