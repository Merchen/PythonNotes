# encoding: UTF-8


"""
配置文件存储常量
"""
from configparser import ConfigParser

CONFIG_FILE = './document/__config.ini'

def read_config():
    config = ConfigParser()
    config.read(CONFIG_FILE)
    for type in config.keys():
        for key in config[type]:
            print ('%s:%s' %(key, config[type][key]))

if __name__ == '__main__':
    read_config()