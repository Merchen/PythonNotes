
# 数据库重构耗时、风险高、成本高

"""
Table: Person
    --------------------
    ID          Person
    --------------------
    1	        Alice
    2	        Bob
    99	        Zach

Table: PersonFriend
    --------------------
    PersonID    FriendID
    --------------------
    1	        2
    2	        1
    2	        99
    99	        1

目标: 查找Bob的朋友

Method1:
    SELECT Person.Person FROM
    (
    SELECT t2.FriendID
    FROM Person t1, PersonFriend t2
    WHERE t1.ID = t2.PersonID AND t1.Person='Bob'
    ) AS Bob, Person
    WHERE Person.ID = Bob.FriendID

Method2:
    SELECT T3.Person
    FROM Person T1
    JOIN PersonFriend T2
    ON T1.ID = T2.PersonID
    JOIN Person T3
    ON T3.ID = T2.FriendID
    WHERE T1.Person = 'Bob'

Method3:
    SELECT T1.Person
    FROM Person T1
    JOIN PersonFriend T2
    ON T1.ID = T2.FriendID
    JOIN Person T3
    ON T2.PersonID = T3.ID
    WHERE T3.Person = 'Bob'

"""

"""
创建节点
CREATE (var:label{key:value,...}), (...) 

CREATE 
(shakespeare:Author {firstname:'William', lastname:'Shakespeare'}),
(juliusCaesar:Play {title:'Julius Caesar'})
# ,....
"""

import pandas as pd
from itertools import count
a = pd.DataFrame([['1\'2', '3\\4', 3], [4, 5, 6]])

a.replace(r"('|\\)", r"\\\1", regex=True, inplace=True)

import pymysql


def load_data(db, table, columns, num=1):
    """从数据库中分批读入数据"""
    conn = pymysql.connect(host='127.0.0.1', port=3306, database=db, user='root', password='123456')

    base = 'SELECT %s FROM %s LIMIT %d ' % (','.join(columns), table, num)
    # 0,1,2,...
    for i in count(0, 1):
        sql = base + 'OFFSET %d;' % (num * i)
        df = pd.read_sql_query(sql, conn)
        if df.empty:
            conn.close()
            raise StopIteration
        else:
            yield df

# columns = ['cust_id', 'cust_name']
# table = 'customers'
# db = 'mydb'
#
# for i in load_data(db, table, columns, 2):
#     print(i)

from py2neo import Graph
import time
import numpy as np
graph = Graph(uri='http://localhost:7474', username='neo4j', password='123456')

graph.delete_all()
tmc = time.time()
for i in range(10):
    print(i)
    keys = list('abcdefghij')
    batch = []
    for _ in range(500):
        values = np.random.rand(10)

        base = '{' + ','.join('%s:%s' % (k, v) for k, v in zip(keys, values)) + '}'
        batch.append(base)
    batch = '[' + ','.join(batch) + ']'

    # print(batch)

    cql = \
          'UNWIND %s as batch ' \
          'MERGE (node1:NODE{a:batch.a, b:batch.b, c:batch.c}) ' \
          'MERGE (node2:NODE{a:batch.d, b:batch.e, c:batch.f}) ' \
          'MERGE (node1) - [:RELATION{g:batch.g}] -> (node2) '% batch


    print(i)
    tm = time.time()
    graph.run('CREATE INDEX ON :NODE(a,b,c,g)')
    graph.run(cql)
    print(time.time()-tm)
    # 快速导入教程
    # https://neo4j.com/developer/guide-import-csv/#_super_fast_batch_importer_for_huge_datasets
print(time.time()-tmc)