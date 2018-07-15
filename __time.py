
import time as tm
from datetime import datetime, date, time, timedelta

########################################################################
###  time   Datetime
########################################################################
def fun1():

    SECS = 1529239510.737           # 自1970-01-01 00:00:00 UTC以来的秒数

    # 日期元组字段(0,Year),(1,Month),(2,Day)，(3,Hour)，(4,Minute)，(5,Second)，(6,Week)...
    TUP, YEAR, MONTH, DAY = (2018,6,17,20,45,10,6,168,0), 2018, 6 , 17

    ISO_TM = '2018-06-17 20:45:10'
    ISO_FORMAT = '%Y-%m-%d %H:%M:%S'

    C_TM = 'Sun Jun 17 20:45:10 2018'
    C_FORMAT = '%a %b %d %H:%M:%S %Y'

    DATE_TIME, DATE, TIME = datetime(2018,6,17,20,45,10), date(2018,6,17), time(20,45,10)

    tm.time()            # 1529239510.737
    tm.localtime(SECS)   # 本地秒数转换为本地时间元组对象
    tm.gmtime(SECS)      # 本地秒数转换为UTC时间元组对象

    tm.mktime(TUP)       # 本地元组到本地秒, 1529239510.0
    tm.ctime(SECS)       # 本地秒到本地字符串， 'Sun Jun 17 20:45:10 2018'
    tm.asctime(TUP)      # 本地元组到本地字符串， 'Sun Jun 17 20:45:10 2018'

    tm.strftime(ISO_FORMAT, TUP)        # 元组到指定格式， '2018-06-17 20:45:10'
    tm.strptime(ISO_TM, ISO_FORMAT)     # 指定格式到元组
    ### time.struct_time(tm_year=2018,tm_mon=6,tm_mday=17,tm_hour=20,tm_min=45,tm_sec=10,tm_wday=6,tm_yday=168,tm_isdst=-1)

    tm.ctime(SECS - 3600 * 10)         # 时间减10时， 'Sun Jun 17 10:45:10 2018'

    datetime.now()                     # 类方法, 返回当前本地datetime对象
    datetime.utcnow()                  # 类方法，返回当前UTC datetime对象

    datetime.combine(DATE,TIME)        # 类方法, 由日期和时间返回datetime对象, datetime.datetime(2018, 6, 17, 20, 45, 10)

    datetime.strptime(ISO_TM,ISO_FORMAT) # 类方法, 返回datetime对象, datetime.datetime(2018, 6, 17, 20, 45, 10)
    datetime.strptime(C_TM,C_FORMAT)     # datetime.datetime(2018, 6, 17, 20, 45, 10)

    datetime.fromtimestamp(SECS)       # 类方法，返回本地datetime对象, datetime.datetime(2018, 6, 17, 20, 45, 10, 737000)
    datetime.utcfromtimestamp(SECS)    # 类方法， 返回UTC datetime对象

    DATE_TIME.ctime()                  # 返回日期字符串, 'Sun Jun 17 20:45:10 2018'

    DATE_TIME.isoformat(sep='T')       # 返回标准日期字符串, '2018-06-17T20:45:10'
    DATE_TIME.strftime(ISO_FORMAT)     # 返回指定格式的日期字符串, '2018-06-17 20:45:10'


    DATE_TIME - timedelta(days=1)      # 返回运算后的datetime对象, datetime.datetime(2018, 6, 16, 20, 45, 10)

    DATE_TIME.timetuple()              # 返回time对象的本地日期元组
    # time.struct_time(tm_year=2018,tm_mon=6,tm_mday=17,tm_hour=20,tm_min=45,tm_sec=10,tm_wday=6,tm_yday=168,tm_isdst=-1)
    timedelta.total_seconds()

    # Datetime对象减10分钟
    DATE_TIME = datetime.fromtimestamp((tm.mktime(DATE_TIME.timetuple())-600))  # datetime.datetime(2018, 6, 17, 20, 35, 10)

    # Datetime对象减10分钟
    ctup = tm.strptime(DATE_TIME.ctime(), C_FORMAT)
    DATE_TIME = datetime.fromtimestamp(tm.mktime(ctup)-600)        # datetime.datetime(2018, 6, 17, 20, 25, 10)