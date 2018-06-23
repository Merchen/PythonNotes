# -*- coding: utf-8 -*-


import pandas as pd
from pymongo import MongoClient
from pymongo.cursor import Cursor
from os.path import basename

"""
db = conn.get_database(dbname)
collection = db.get_collection(collectionname)
"""

MONGO_URL = "127.0.0.1:27017"

DATA_BASE = "VnTrader_Trade_Raw_Db"

OUT_PATH = r'C:\Users\MERLIN\Desktop\Python'

########################################################################
###  连接至mongodb，返回连接对象
########################################################################
def connect2mongodb(host=None, port=None):
    return MongoClient(host, port)


########################################################################
###  collection转为csv
########################################################################
def collection2csv(coll, csv_name=None, query_args=None):
    """
    将集合输出至csv，可制定筛选条件和文件名称和路径
    
    Parameters
    ----------
    coll: 已连接的集合名称
    csv_name: 目标csv文件的路径与名称
    query_args: 查找条件，默认全部导出
    
    """
    if query_args is None:
        query_args = {}
    df = pd.DataFrame(list(coll.find(query_args)))
    if csv_name is None:
        csv_name = '%s-%s.csv' %(coll.database.name, coll.name)
    df.to_csv(csv_name, index=False, encoding='utf-8')


########################################################################
###  csv转为collection
########################################################################
def csv2collection(db, csv_name, coll_name=None, ignore_id=True,
                   drop_exist=False):
    """
    将csv添加至数据库，可指定csv路径和新的集合名称
    
    Parameters
    ----------
    db：已完成连接的数据库
    csv_name: csv文件路径，包含名称及后缀
    coll_name: 还原后新的集合名称
    ignore_id: 是否删除csv中的'_id'列（含ObjectId信息，不可重复），对于不含_id信息的文档，系统会自动添加
    drop_exist: 若同名集合存在是否删除
    """
    if coll_name is None:
        coll_name = basename(csv_name).rstrip('.csv')

    df = pd.read_csv(csv_name, header=0)
    if ignore_id:
        if '_id' in df.columns:
            df.drop('_id', axis=1, inplace=True)
    df.fillna('', inplace=True)

    if drop_exist:
        db[coll_name].drop()
    db[coll_name].insert_many(df.T.to_dict().values())

    # 插入新集合,json将Dataframe更改为dictionary，导致行顺序不定
    # import json
    # db[coll_name].insert_many(json.loads(df.T.to_json()).values())

    # 直接插入时，Dataframe中的数字无法直接插入数据库
    # del doc['orderID']
    # doc['orderID'] = int(doc['orderID'])


if __name__ == '__main__':

    conn = connect2mongodb()

    db = conn.get_database(DATA_BASE)

    coll = db.get_collection('CTP-090923')

    cur = Cursor(coll)

    print(coll.find({}).count())

    pass