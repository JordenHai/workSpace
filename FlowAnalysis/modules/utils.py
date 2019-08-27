# _*_coding:utf-8_*_
__author__ = "Alex Li"


from conf import settings
import os
import yaml
import json

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def print_err(msg, quit=False):
    output = "\033[31;1mError: %s\033[0m" % msg
    if quit:
        exit(output)
    else:
        print(output)


def yaml_parser(yml_filename):
    """
    load yaml file and return
    :param yml_filename:
    :return:
    """
    # yml_filename = "%s/%s.yml" % (settings.StateFileBaseDir,yml_filename)
    try:
        yaml_file = open(yml_filename, "r")
        data = yaml.load(yaml_file)
        return data
    except Exception as e:
        print_err(e)


def loadFiles(filepath):
    f = open(filepath, encoding="utf-8")
    strs = f.readlines()
    return strs


def jsonData(source_data):
    dicts = {}
    for index, line in enumerate(source_data):
        dict = {}
        list = line.split(",")
        for val in list:
            tagName = val.split("=")[0].strip()
            tagValue = val.split("=")[1].strip()
            dict[tagName] = tagValue
        dicts[list[0].split("=")[1].strip()] = dict
    print(dicts)
    json_data = json.dumps(
        dicts, sort_keys=True, indent=4, separators=(",", ": ")
    ).encode("utf-8")
    return json_data

def dumpFiles(filepath,source_data):
    # print(os.path.dirname(os.path.abspath(filepath)))
    file = os.path.dirname(os.path.abspath(filepath)) + "\\meta.json"
    f = open(file, "wb")
    f.write(source_data)
    return file

def json_parser(filepath):
    print(filepath)
    # print(settings.BASE_DIR + filepath)
    file = os.path.abspath(filepath)
    strs_data = loadFiles(file)
    json_data = jsonData(strs_data)
    json_file = dumpFiles(filepath,json_data)
    return json_file

