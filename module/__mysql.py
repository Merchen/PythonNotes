# -*- coding: utf-8 -*-

import pymysql
import pandas as pd

# 建立数据库连接, 若无法连接需更改连接方式, 如下:
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'
# db = pymysql.connect(host='127.0.0.1',port=3306,user= 'root',password='123456' )

# 使用操作游标
# db.db = 'mydb'
# print db.select_db('mydb')
# cursor = db.cursor()
# query = 'SELECT * FROM products'
# execute查询, 返回查询结果数
# res_num = cursor.execute(query)
# print res_num
# 获取全部数据
# allData = cursor.fetchall()
# oneData = cursor.fetchone()
# cursor.close()

class MySQLConnector():
    """自定义python连接mysql"""
    def __init__(self,host,port,user,password,db=None):

        # 连接函数引用
        self.__conn = self.connect(host=host, port=port, user=user, password=password, db=db)

        # 游标对象
        self.__cursor = self.conn.cursor()


    @property
    def conn(self):
        return self.__conn


    def connect(self, host,port,user,password,db):
        conn = pymysql.connect(host=host, port=port, user=user, password=password,
                                      db=db, charset='utf8')
        return conn

    def __getitem__(self,dbname):
        """以conn[dbname]方式引用数据库"""
        if dbname is None:
            return
        if dbname in self.getDBNames():
            self.__conn.select_db(dbname)
        else:
            raise ValueError('Wrong DB name!')
        return self

    def getDBNames(self):
        """获取连接中当前所有数据库名称"""
        self.__cursor.execute('SHOW DATABASES')
        dbnames = []
        for dbname in self.__cursor.fetchall():
            dbnames.append(dbname[0])
        return dbnames

    def getDBTables(self):
        """获取当前数据库所有表"""
        tables = []
        try:
            self.__cursor.execute('SHOW TABLES')
            for table in self.__cursor.fetchall():
                tables.append(table[0])
        except Exception as err:
            print("Error: %s" %err)
        return tables

    def getTableColumns(self,table):
        """获取指定表的列标签"""
        columns = []
        try:
            if table in self.getDBTables():
                self.__cursor.execute('SHOW COLUMNS FROM %s' %table)
                for column in self.__cursor.fetchall():
                    columns.append(column[0])
        except Exception as err:
            print("Error: %s" % err)
        return columns

    def read2pandas(self,query):
        """查询结果转为pandas"""
        try:
            df = pd.read_sql(query,self.conn)
            return df
        except Exception as err:
            raise err

    def execute(self,query):
        """执行SQL语句并返回Cursor对象"""
        self.__cursor.execute(query)
        return self.__cursor

    def commit(self):
        self.conn.commit()


# res = mysql.execute('select * from customers')

#==customers============================================================================================
#       cust_id cust_name       cust_address        cust_city   cust_state  cust_zip    cust_courty     cust_email
# 0     10001	Coyote Inc.	    200 Maple Lane	    Detroit	    MI	        44444	    USA	Y Lee	    ylee@coyote.com
# 1     10002	Mouse House	    333 Fromage Lane	Columbus	OH	        43333	    USA	Jerry Mouse
# 2     10003	Wascals	        1 Sunny Place	    Muncie	    IN	        42222	    USA	Jim Jones	rabbit@wascally.com
# 3     10004	Yosemite Place	829 Riverside Drive	Phoenix	    AZ	        88888	    USA	Y Sam	    sam@yosemite.com
# 4     10005	E Fudd	        4545 53rd Street	Chicago	    IL	        54545	    USA	E Fudd

#==orderitems============================================================================================
#     order_num  order_item prod_id  quantity  item_price
# 0       20005           1   ANV01        10        5.99
# 1       20005           2   ANV02         3        9.99
# 2       20005           3    TNT2         5       10.00
# 3       20005           4      FB         1       10.00
# 4       20006           1  JP2000         1       55.00
# 5       20007           1    TNT2       100       10.00
# 6       20008           1      FC        50        2.50
# 7       20009           1      FB         1       10.00
# 8       20009           2     OL1         1        8.99
# 9       20009           3   SLING         1        4.49
# 10      20009           4   ANV03         1       14.99

#==orders================================================================================================
#    order_num      order_date      cust_id
# 0      20005      2005-09-01      10001
# 1      20006      2005-09-12      10003
# 2      20007      2005-09-30      10004
# 3      20008      2005-10-03      10005
# 4      20009      2005-10-08      10001

#==products==============================================================================================
#    prod_id  vend_id       prod_name  prod_price       prod_desc
# 0    ANV01     1001    .5 ton anvil        5.99       .5 ton anvil, black, complete with handy hook
# 1    ANV02     1001     1 ton anvil        9.99       1 ton anvil, black, complete with handy hook a...
# 2    ANV03     1001     2 ton anvil       14.99       2 ton anvil, black, complete with handy hook a...
# 3    DTNTR     1003       Detonator       13.00       Detonator (plunger powered), fuses not included
# 4       FB     1003       Bird seed       10.00       Large bag (suitable for road runners)
# 5       FC     1003         Carrots        2.50       Carrots (rabbit hunting season only)
# 6      FU1     1002           Fuses        3.42       1 dozen, extra long
# 7   JP1000     1005    JetPack 1000       35.00       JetPack 1000, intended for single use
# 8   JP2000     1005    JetPack 2000       55.00       JetPack 2000, multi-use
# 9      OL1     1002        Oil can\        8.99       Oil can, red
# 10    SAFE     1003            Safe       50.00       Safe with combination lock
# 11   SLING     1003           Sling        4.49       Sling, one size fits all
# 12    TNT1     1003   TNT (1 stick)        2.50       TNT, red, pack of 10 sticks
# 13    TNT2     1003  TNT (5 sticks)       10.00       TNT, red, pack of 10 sticks

#==vendors===============================================================================================
#    vend_id       vend_name     vend_address    vend_city vend_state vend_zip    vend_country
# 0     1001     Anvils R Us  123 Main Street   Southfield         MI    48075    USA
# 1     1002     LT Supplies  500 Park Street      Anytown         OH    44333    USA
# 2     1003            ACME  555 High Street  Los Angeles         CA    90046    USA
# 3     1004    Furball Inc.  1000 5th Avenue     New York         NY    11111    USA
# 4     1005         Jet Set   42 Galaxy Road       London       None  N16 6PS    England
# 5     1006  Jouets Et Ours  1 Rue Amusement        Paris       None    45678    France

#######################################################################
###  查询SELECT  db.read2pandas(query)
#######################################################################
#
# 排序并限制输出--price最高的前5行
# LIMIT子句必须位于ORDER BY之后（若存在）
query1 = 'SELECT prod_id, prod_price ' \
         'FROM products ' \
         'ORDER BY prod_price DESC ' \
         'LIMIT 5;'

# ORDER BY--第3-7行
query2 = 'SELECT products.prod_name ' \
         'FROM mydb.products ' \
         'LIMIT 2,5;'

# ORDER BY 降序
query3 = 'SELECT prod_id, prod_price ' \
         'FROM products ' \
         'ORDER BY prod_price DESC, prod_id;'

# WHERE--获取price大于等于10.0的行
query4 = 'SELECT prod_id, prod_price ' \
         'FROM products ' \
         'WHERE prod_price >= 10.0 ' \
         'ORDER BY prod_price DESC;'

# WHERE --多限制条件, AND > OR
query5 = 'SELECT prod_id, prod_price ' \
         'FROM products ' \
         'WHERE prod_price BETWEEN 10 AND 40.0 AND vend_id IN (1002,1001) ' \
         'ORDER BY prod_price DESC;'

# LIKE -- 通配符表达式需用''包围, '%'匹配任意字符任意次数, '_'匹配单个字符
# 通配符搜索处理时间较长
query6 = 'SELECT prod_id, prod_name ' \
         'FROM products ' \
         'WHERE prod_name LIKE \'jet%\' OR prod_name LIKE \'_ ton%\';'

# REGEXP -- 正则表达式
# 默认不区分大小写, 可使用BINARY声明区分大小写
# 匹配'.'的表达式为'\\\.', 输入到SQL中为'\\.', SQL输入到正则表达式为'\.'
# 匹配'\'的表达式为'\\\\\\\\', 输入到SQL中为'\\\\', SQL输入到正则表达式为'\\'
query7 = 'SELECT prod_id, prod_name ' \
         'FROM products ' \
         'WHERE prod_name REGEXP "([123] ton)|pack|\\\\\\\\";'

#######################################################################
###  拼接Concat与列别名AS  db.read2pandas(concat)
#######################################################################
#
# 拼接为一列
concat1 = "SELECT Concat(vend_name, '(', vend_country, ')') AS profile " \
          "FROM vendors " \
          "ORDER BY vend_name;"

concat2 = "SELECT prod_id, quantity, item_price , quantity*item_price as expanded_price " \
          "FROM orderitems " \
          "WHERE order_num = 20005;"

#######################################################################
###  函数
#######################################################################
#
func1  = 'SELECT cust_id, order_num, order_date ' \
         'FROM orders ' \
         'WHERE Date(order_date) BETWEEN \'2005-09-01\' AND \'2005-09-30\';'

func2  = 'SELECT cust_id, order_num, order_date ' \
         'FROM orders ' \
         'WHERE Year(order)=2005  AND Month(order_date)=10;'

#######################################################################
###  聚合与分组GROUP BY
#######################################################################
# GROUP BY必须在WHERE语句之后
aggr1 = 'SELECT AVG(prod_price) AS avg_price ' \
        'FROM products ' \
        'WHERE vend_id = 1003;'

# 返回max_price的最大值、最小值、均值
aggr2 = 'SELECT MAX(prod_price) AS max_price, ' \
        'MIN(prod_price) AS min_price, ' \
        'COUNT(*) AS count ' \
        'FROM products;'

# 返回每个vend_id出现的次数, 并逆序排序
group1 = 'SELECT vend_id, COUNT(*) AS num_prods ' \
         'FROM products ' \
         'GROUP BY vend_id ' \
         'ORDER BY num_prods DESC;'

# 返回每个vend_id出现的次数, 并逆序排序
group2 = 'SELECT vend_id, COUNT(*) AS num_prods ' \
         'FROM products ' \
         'GROUP BY vend_id ' \
         'ORDER BY num_prods DESC;'

# HAVING对分组后的数据过滤。WHERE在分组前进行过滤, HAVING在分组后过滤
group3 = 'SELECT cust_id, COUNT(*) AS orders ' \
         'FROM orders ' \
         'GROUP BY cust_id ' \
         'HAVING COUNT(*) >= 2;'

#######################################################################
###  子查询IN/=/<>
#######################################################################
# 执行由内至外查询, 内查询仅返回一列
#
# 子查询获取orderitems中prod_id = "TNT2"的order_num, 外查询将内查询的返回order_num作为条件, 以查找所有满足条件的行
subquery1 = 'SELECT cust_id, order_num ' \
            'FROM orders ' \
            'WHERE order_num IN(' \
                'SELECT order_num ' \
                'FROM orderitems ' \
                'WHERE prod_id = "TNT2");'

subquery2 = 'SELECT cust_id,cust_name,cust_contact ' \
            'FROM customers ' \
            'WHERE cust_id IN( ' \
                'SELECT cust_id ' \
                'FROM orders  ' \
                'WHERE order_num IN( ' \
                    'SELECT order_num ' \
                    'FROM orderitems ' \
                    'WHERE prod_id = "TNT2"));'

# orders.cust_id = customers.cust_id解决列名多义性
subquery3 = 'SELECT cust_name, cust_state, cust_id, ' \
                    '(SELECT COUNT(*) ' \
                    'FROM orders ' \
                    'WHERE orders.cust_id = customers.cust_id) AS orders ' \
            'FROM customers ' \
            'ORDER BY orders DESC;'

#######################################################################
###  表连接
#######################################################################
# 没有WHERE条件时, 返回多个表的笛卡尔积
#
# 等值连接--对于多个表若存在重复列名, 需使用完全限定表名
joint1 = 'SELECT vendors.vend_id, vend_name, prod_name, prod_price ' \
         'FROM vendors, products ' \
         'WHERE vendors.vend_id = products.vend_id ' \
         'ORDER BY vend_id, prod_price;'

# 内部连接--与等值连接一致
joint2 = 'SELECT vend_name, prod_name, prod_price ' \
         'FROM vendors INNER JOIN products ' \
         'ON vendors.vend_id = products.vend_id;'

joint3 = 'SELECT prod_name, prod_price, quantity, vend_name ' \
         'FROM orderitems, products, vendors ' \
         'WHERE products.vend_id = vendors.vend_id ' \
                'AND orderitems.prod_id = products.prod_id ' \
                'AND order_num = 20005;'

# orderitems: order_num、order_item、prod_id、quantity
# products: prod_id、vend_id、prod_name、prod_price、prod_desc
# vendors: vend_id、vend_name、vend_address、vend_city、vend_state vend_zip、vend_country
# 获取orderitems.order_num=20005的订单信息
# 由orderitems.vend_id = products.vend_id添加products.prod_price
# 由products.prod_id = vendors.prod_id添加vendors.vend_name
# 结果与上方使用WHERE语句一致
joint4 = 'SELECT orderitems.quantity, products.prod_name, products.prod_price, vendors.vend_name ' \
         'FROM orderitems ' \
         'INNER JOIN products ON orderitems.prod_id = products.prod_id ' \
         'INNER JOIN vendors ON vendors.vend_id = products.vend_id ' \
         'WHERE order_num = 20005'

# 子查询
joint5 = 'SELECT vend_id, prod_id, prod_name ' \
         'FROM products ' \
         'WHERE vend_id = (SELECT vend_id FROM products WHERE prod_id = "DTNTR");'

# 自连接--效率比子查询高
joint6 = 'SELECT p1.vend_id, p1.prod_id, p1.prod_name ' \
         'FROM products AS p1, products AS p2 ' \
         'WHERE p1.vend_id = p2.vend_id AND p2.prod_id = "DTNTR";'


# 外部连接--相关表中没有的数据以NaN表示, RIGHT和LIFT指定基准表(返回包含基表的所有行)
joint7 = 'SELECT c.cust_id, o.order_num ' \
         'FROM customers AS c LEFT JOIN orders AS o ' \
         'ON c.cust_id = o.cust_id;'

# 聚合连接--检查所有客户的订单数
# 客户信息表customers, 订单信息表orders
joint8 = 'SELECT c.cust_id, cust_name, COUNT(o.order_num) AS num_ord ' \
         'FROM customers AS c LEFT JOIN orders AS o ON o.cust_id = c.cust_id ' \
         'GROUP BY o.cust_id;'

#######################################################################
###  复合查询UNION（并查询、组合查询）
#######################################################################
# 单个查询在不同表返回类似的相同数据
# 单个表执行多个查询，并按按个查询结果返回
# 返回结果自动去重, 使用UNION ALL声明返回重复行, WHERE不能实现这种效果
#
union1 = 'SELECT vend_id, prod_id, prod_price ' \
         'FROM products ' \
         'WHERE prod_price <= 5 ' \
         'UNION ' \
         'SELECT vend_id, prod_id, prod_price ' \
         'FROM products ' \
         'WHERE vend_id IN (1001, 1002)'

# 简单的UNION连接可使用WHERE语句的OR逻辑替代
union2 = 'SELECT vend_id, prod_id, prod_price ' \
         'FROM products ' \
         'WHERE prod_price <= 5 OR vend_id IN (1001, 1002)' \

#######################################################################
###  全文本搜索FULL_TEXT MATCH AGAINST
#######################################################################
# 搜索结果自动排序, 匹配程度好的优先返回

text1 = 'SELECT note_text ' \
        'FROM productnotes ' \
        'WHERE MATCH(note_text) AGAINST("rabbit")'

# 查询拓展
# 执行两次查询，第一次执行普通的全文本搜索; 第二次将第一次搜索结果的词作为参考对象，重新搜索以找到与搜索结果具有相关性的行
text2 = 'SELECT note_text ' \
        'FROM productnotes ' \
        'WHERE MATCH(note_text) AGAINST("rabbit" WITH QUERY EXPANSION)'

# 布尔表达式--返回包含heavy单词且不包含以rope为开头的单词的行
text3 = 'SELECT note_text ' \
        'FROM productnotes ' \
        'WHERE MATCH(note_text) AGAINST("+heavy -rope*" IN BOOLEAN MODE);'

#######################################################################
###  插入数据INSERT INTO
#######################################################################
#
# 主键为自动递增, 插入部分列, 无元素的列值为空
insert1 = "INSERT INTO customers(cust_name, cust_address, cust_city) " \
          "VALUES('Coyote Inc.', '200 Maple Lane', 'Detroit');"


#######################################################################
###  更新UPDATE与 删除DELETE
#######################################################################
# update要严格限制更新条件, 防止更新全部表
# 被其他表作为外键引用时, 不可直接删除
#
update1 = "UPDATE customers " \
          "SET cust_email = 'elemer@fudd.com', cust_name = 'The Fudds' " \
          "WHERE cust_id = 10005;"

delete1 = "DELETE FROM customers " \
          "WHERE cust_id = 10001"

#######################################################################
###  创建、修改表
#######################################################################
# 主键值不为空且主键值不唯一（多个主键时, 满足组合值不唯一即可）
# 可指定默认值、自定增量等
# InnoDB支持事务处理的引擎, 但不支持全文本搜索; MyISAM性能高, 支持全文本搜索, 但不支持事务处理(一般为默认引擎);
#
create1 = 'CREATE TABLE testTable (' \
          'cust_id          INT         NOT NULL AUTO_INCREMENT, ' \
          'cust_name        CHAR(50)    NOT NULL, ' \
          'cust_address     CHAR(50)    NULL, ' \
          'cust_country     CHAR(50)    NULL DEFAULT "China", ' \
          'PRIMARY KEY (cust_id, cust_name) ' \
          ') ENGINE=InnoDB;'

# 增加列
alter1 = 'ALTER TABLE testTable ' \
         'ADD cust_gender CHAR(20), cust_gender1 CHAR(20)'

# 删除列
alter2 = 'ALTER TABLE testTable ' \
         'DROP COLUMN cust_gender;'

# 重命名表
rename1 = 'RENAME TABLE testTable TO test1;'

#######################################################################
###  视图
#######################################################################
# 视图仅是引用副本, 原值改变时, 视图中的值也会发生改变
# 对视图进行更新相当于更新基表

# 创建视图, OR REPLACE表示不存在时创建, 存在时重置
view1 = 'CREATE OR REPLACE VIEW productcustomers AS  \
        ( \
        SELECT cust_name, cust_contact, order_num  \
        FROM customers, orders  \
        WHERE customers.cust_id = orders.cust_id  \
        );'

# 删除视图
view2 = 'DROP VIEW productcustomers'

#######################################################################
###  存储过程
#######################################################################
#
drop1 = 'DROP PROCEDURE IF EXISTS p1;'

# MySQLdb execute can craete procedure
proc1 = "\
    CREATE PROCEDURE p1() \
    BEGIN  \
        SELECT products.vend_id, vend_name, COUNT(products.vend_id) AS count_id  \
        FROM products  \
        INNER JOIN vendors  \
        ON vendors.vend_id = products.vend_id \
        GROUP BY vend_id;  \
    END; "

# 带参数的存储过程
drop2 = 'DROP PROCEDURE IF EXISTS p2;'
proc2 = ' \
    CREATE PROCEDURE p2( \
        OUT pmin DECIMAL(8,2),  \
        OUT pmax DECIMAL(8,2)) \
    BEGIN \
        SELECT MIN(prod_price) INTO pmin FROM products; \
        SELECT MAX(prod_price) INTO pmax FROM products; \
    END ;'
call2 = 'CALL p2(@pmin, @pmax);'
select2 = 'SELECT @pmin, @pmax'
# mysql.execute(drop2)
# mysql.execute(proc2)
# mysql.execute(call2)
# print mysql.read2pandas(select2)

#######################################################################
###  触发器TRIGGER
#######################################################################
# 执行更新、插入、删除等动作时，系统自动执行触发器
#
dropTrigger1 = 'DROP TRIGGER IF EXISTS t1;'

# 插入数据时自动更新用户的email信息
createTrigger1 = " \
    CREATE TRIGGER t1 BEFORE INSERT ON customers \
    FOR EACH ROW \
    BEGIN \
        IF NEW.cust_email IS NULL THEN \
            SET NEW.cust_email = CONCAT(NEW.cust_name, '@google.com'); \
        END IF; \
    END ;"

#######################################################################
###  事务处理
#######################################################################
#
# SELECT * FROM customers;
# START TRANSACTION;
# DELETE FROM customers;
# ROLLBACK;
# SELECT * FROM customers;

mysql = MySQLConnector(host='127.0.0.1',port=3306,user= 'root',password='123456')
mysql.conn.select_db('mydb')
# db = mysql['mydb']
mysql.commit()
# print db.getDBTables()
# print db.getTableColumns('customers')
# print db.read2pandas(insert1)
