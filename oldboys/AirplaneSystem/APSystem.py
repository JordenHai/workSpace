import random
import json

# station = ["beijing","shanghai","nanjing","hangzhou","wuxi","ningbo","qingdao","wenzhou","shenzhen","tianjing"]
# stationID = ['10010','10011','10012','10013','10014','10015','10016','10017','10018','10019',"10020"]
# weekdays = ["Mon","Tues","Wed","Thurs","Fri","Sat",'Sun']

# def init():
#     # 每次使用的d 必须是临时变量 不能定义成全局变量
#     for i in range(10):
#         d = {}
#         src = int(random.random() * 10)
#         d['FightID'] = stationID[i]
#         d['StaStat'] = station[src]
#         des = int(random.random() * 10)
#         des = (src + des) // 2
#         if des == src and des <= 9:
#             des = src + 1
#         else:
#             des = src // 2 -1
#         d['EndStat'] = station[des]
#         m = int(random.random() * 10) // 2
#         d['DataSch'] = weekdays[m]
#         planeSet.append(d)

def uploadFile(fileName,planeSet):

    fp = open(fileName,'wb')
    data = json.dumps(planeSet).encode('utf-8')
    fp.write(data)
    fp.close()
    pass

def loadFile(fileName):
    fp = open(fileName,'rb')
    data = fp.readline()
    planeSet = json.loads(data)
    return planeSet
    pass

def displayTicket(planeSet):
    print("\033[41;1mSTART     END      TIME \033[0m")
    for res in planeSet:

        print("\033[2;31;42;1m{:<9} {:<8} {:<5}\033[0m".format(res['StaStat'],res['EndStat'],res['DataSch']))
    pass

def addFligtINFO(planeSet):
    d = {}
    res = input("-->")
    pass

if __name__ == "__main__":
    # init()
    # print(planeSet)
    # uploadFile('planeSchedule',planeSet)
    planeSet = []
    planeSet = loadFile('planeSchedule')
    # print(planeSet)
    displayTicket(planeSet)
    res = input("==>")
    print(res,type(res))