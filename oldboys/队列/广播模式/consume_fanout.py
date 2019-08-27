# 消费者 只是会从q中取出消息
#                ------[]------
#    EX1         ------[]------    CONSUMER
#                ------[]------
#                []
#    EX2         []
#                []
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')

result = channel.queue_declare(queue='',exclusive=True)#exclusive 排他的，唯一的 不指定queue名字 rabbit会随
# 机分配一个 自动删除

queue_name = result.method.queue
print('qname:',queue_name)

def callback(ch,method,properties,body):
    print("[x] %r"%body)

#消息队列绑定转发器
channel.queue_bind(exchange='logs',queue=queue_name)
# amq.gen-Vnkzt7_ntpz9ZK4a84fzhw
print('[*] waiting for logs. To exit press CTRL+C')

channel.basic_consume(queue=queue_name,on_message_callback=callback)
channel.start_consuming()