
import pika
import random
import os
class RpcServer:
    msg_dic = {}
    def __init__(self):
        credentials = pika.PlainCredentials('alex', 'alex3714')
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                            virtual_host='/',
                                            credentials=credentials))
        # self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',))
        self.channel = self.conn.channel()
        result = self.channel.queue_declare(queue='rpc_queue')
        self.queue = result.method.queue
        self.uids = self.cre_uidmsg()

    def execfunction(self,command):
        res = os.popen(command).read()
        msg_id = self.cre_uidmsg()
        self.msg_dic[msg_id] = res
        return msg_id
        pass

    def cre_uidmsg(self):
        ran = []

        for i in range(5):
            value = int(random.random() * 10)
            ran.append(value)
        nums = ran[0] + ran[1] + ran[2] + ran[3] + ran[4]
        return nums

    def check(self,*args):
        ch = args[0]
        method = args[1]
        property = args[2]
        command = args[3]
        id = command.split(' ')[1]
        data = self.msg_dic[id]

        ch.basic_publish(exchange='',
                            routing_key = property.reply_to,
                            properties=pika.BasicProperties(
                                        correlation_id= property.correlation_id),
                            body = str(data))

        self.channel.basic_ack(delivery_tag=method.delivery_tag)
        pass

    def on_request(self,ch,method,property,body):
        command = str(body,'utf-8')
        print(">>:%s"%command)
        com = command.split(' ')[0]
        if hasattr(self,com):
            func = getattr(self,com)
            func(ch,method,property,command)
        else:
            data = self.execfunction(command)
            ch.basic_publish(exchange='',
                             routing_key=property.reply_to,
                             properties=pika.BasicProperties(
                                 correlation_id=property.correlation_id),
                             body=str(data))

            self.channel.basic_ack(delivery_tag=method.delivery_tag)

    def call(self):
        self.channel.basic_qos(prefetch_count=2)
        self.channel.basic_consume(queue=self.queue,
                                   on_message_callback=self.on_request,
                                   auto_ack=False)
        pass
    def start_consume(self):
        self.channel.start_consuming()


if __name__ == "__main__":
    r = RpcServer()
    r.call()
    r.start_consume()    
    pass