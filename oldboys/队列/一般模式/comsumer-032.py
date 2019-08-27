import time
import pika
#轮询机制进行获取
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
    )

channel = connection.channel()

#我们不确定那个一个先运行
#所以我们both declare
channel.queue_declare(queue='hello',durable = True) #声明队列名字


def callback(ch,method,properties,body):#回调函数 事件触发
    print("-->",ch,method,properties)
    time.sleep(4)
    print("[x]",body)
    #手动处理 消息
    ch.basic_ack(delivery_tag= method.delivery_tag)
    pass

channel.basic_qos(prefetch_count=1)

#auto ack  the false is that if the connection is broken the file will send to another
#while the ack is set to the true the data will lose
channel.basic_consume(queue='hello',on_message_callback=callback,auto_ack=False)

print('[*] waiting for messages.To exit press CTRL+C')
channel.start_consuming()

