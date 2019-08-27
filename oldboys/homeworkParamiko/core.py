
import paramiko
import threading
import queue
import json
import time
list = []
def recieveData(data):
    value = json.loads(data)
    list.append(value['host'])
    list.append(value['data'])

    pass

def getHostAndUser():
    host = ["10.20.224.10","10.20.224.20","10.20.224.30","10.20.224.40"]
    user = ["gao-01","gao-02","gao-03","gao-04"]
    return host,user

def initSSH(host,user,event,q):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,port='22',username=user,password='123456')

    while True:

        while q.qsize() >0:
            data = q.get()
            # print(ssh,data)
            # print(type(data))
            # print("------ssh%s------"%ssh)
            stdin, stdout, stderr = ssh.exec_command(data)

            res, err = stdout.read(), stderr.read()
            result = res if res else err
            result = result.decode('utf-8')
            dict = {
                'data':result,
                'host':host
            }
            recieveData(json.dumps(dict).encode('utf-8'))
            event.clear()
        else:
            event.set()

    pass

def hander(host,user,event,q):
    t = threading.Thread(target=initSSH,args=(host,user,event,q))
    t.start()
    return t
    pass

def display():
    print("******************")
    print("                  ")
    print("                  ")
    print("******************")
    pass

def set_up(event,q):

    while True:
        display()
        value = int(input("-->"))
        if value == 1:
            q.put("ls -l")
            q.put("df")
            q.put("ifconfig")
            q.put("ifconfig")
            time.sleep(0.5)
            pass
        elif value == 2:
            pass
        elif value == 3:
            pass
        else:
            pass
        for i in range(0,8,2):
            print(list[i])
            print(list[i+1])
        list.clear()


    pass

def main():
    event = threading.Event()

    # event.clear()
    # event.set()
    # event.is_set()
    # event.wait()

    q = queue.Queue()
    hosts,users = getHostAndUser()
    for index,host in enumerate(hosts):
        t = hander(host,users[index],event,q)

    t = threading.Thread(target=set_up,args=(event,q))
    t.start()
    pass


if __name__ == '__main__':
    main()
    pass
















#
#
# import paramiko
# import threading,queue
# trans = []
# hosts = []
# t_obj = []
# q = queue.Queue()
#
# hostnames = ["10.20.224.10","10.20.224.20","10.20.224.30","10.20.224.40"]
# users = ["gao-01","gao-02","gao-03","gao-04"]
# def run(host,user):
#
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh.connect(hostname=host,port='22',username=user,password='123456')
#     while q.qsize() > 0:
#
#     hosts.append(ssh)
#     print(hosts)
#
#
# for res in enumerate(hostnames):
#     # print(res[0])
#     t = threading.Thread(target=run,args=(hostnames[res[0]],users[res[0]]))
#     t.start()


# def createThread():
#     for res in enumerate(hostnames):
#         # print(res[0])
#         t = threading.Thread(target=run, args=(hostnames[res[0]], users[res[0]]))
#         t.start()
#         t_obj.append(t)
#
# def main():
#     createThread()
#
# if __name__ == '__main__':
#     main()
#     for res in hosts:
#         stdin, stdout, stderr = res.exec_command('df')
#         res, err = stdout.read(), stderr.read()
#         result = res if res else err
#         print(result.decode())