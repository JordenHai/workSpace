import pika
import sys
connection = pika.BlockingConnection(
                pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

messsage = ''.join(sys.argv[2:]) or 'hello world'

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=messsage)

print("[X] sent %r:%r "%(routing_key,messsage))

connection.close()