# _*_coding:utf-8_*_
__author__ = "Jorden Hai"

from modules import models
from modules.db_conn import engine, session
from modules.utils import print_err, json_parser
import json

def syncdb(argvs):
    print("Syncing DB....")
    models.Base.metadata.create_all(engine)  # 创建所有表结构


def create_tables(argvs):
    if "-f" in argvs:
        flowfile = argvs[argvs.index("-f") + 1]
    else:
        print_err(
            "invalid usage, should be:\ncreate_hosts -f <the new hosts file>", quit=True
        )
    json_file = json_parser(flowfile)
    obj_list = []
    with open(json_file, encoding="utf-8") as load_f:
        load_dict = json.load(load_f)

    for key, value in load_dict.items():
        print("key:", key, "value:", value)
        obj = models.PathTag(Packet_in_times=key,Dpid=value['Dpid'],Cookie=value['Cookie'],Source_address=value['Source_address'],Destination_address=value['Destination_address'],Data_len=value['Data_len'])
        obj_list.append(obj)

    print(obj_list)
    models.Base.metadata.create_all(engine)
    for var in obj_list:
        session.add(var)

    session.commit()