#remote procedure call

import pika
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    pass

def on_request(ch,method,property,boby):
    n = int(boby)
    print("[.] fib(%s)"%n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key = property.reply_to,
                     properties=pika.BasicProperties(
                                correlation_id= property.correlation_id),
                     body = str(response))

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='rpc_queue',
                      on_message_callback=on_request)

print("[x]---------------------[x]")

channel.start_consuming()
