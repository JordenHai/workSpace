import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(queue='',exclusive=True)

queue_name = result.method.queue

bindingKeys = sys.argv[1:]
if not bindingKeys:
    sys.stderr.write("Usage:%S [bindingkey]..\n"%sys.argv[0])

    sys.exit(1)

for bindingkey in bindingKeys:
    channel.queue_bind(queue=queue_name,exchange='topic_logs',routing_key=bindingkey)


print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue=queue_name,on_message_callback=callback)

channel.start_consuming()