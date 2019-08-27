import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
    )

channel = connection.channel()  #声明一个管道

#声明 queue  durable= True 意思持久化队列
channel.queue_declare(queue='hello',durable=True)

#当exchange为空时 消息只会被发送到一个consumer，不是广播模式
#fanout  所以bind到exchange的queue都可以收到
#
#
#
#direct 通过routingkey和exchange决定哪一个唯一的queue可以接收消息
#topic所有妇科routingkey的才可以bind到queue的消息
channel.basic_publish(exchange='',
                      routing_key='hello',#queue名字
                      body='Hello World',
                      properties=pika.BasicProperties(
                          delivery_mode=2,)#make the message persistent
                    )

print("[x] ----->>>>>>")
connection.close()

#当前模式下，