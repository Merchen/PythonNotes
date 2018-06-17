# -*- coding: utf-8 -*-

########################################################################
###  time
########################################################################
#
# time()      - > 返回本地时间秒数
# gmtime()    - > 秒转换为UTC时间元组
# localtime() - > 秒转换为本地时间元组
# ctime()     - > 秒转换为本地时间字符串
# asctime()   - > 元组转换为本地时间字符串
# mktime()    - > 本地时间元组转换为自纪元以来的秒
# sleep()     - > 睡眠(秒)
# strftime()  - > 根据格式规范将时间元组转换为字符串
# strptime()  - > 根据格式规范将字符串解析为时间元组
#
# 日期元组字段(0,Year),(1,Month),(2,Day)，(3,Hour)，(4,Minute)，(5,Second)，(6,Week)...

from time import *

secs = time()               # 1529239510.737
secs = 1529239510.737
tup = localtime(secs)       # 本地时间元组
gmtime(secs)
### time.struct_time(tm_year=2018,tm_mon=6,tm_mday=17,tm_hour=12,tm_min=45,tm_sec=10,tm_wday=6,tm_yday=168,tm_isdst=0)

mktime(tup)                 # 本地元组到本地秒, 1529239510.0
ctime(secs)                 # 本地秒到本地字符串， 'Sun Jun 17 20:45:10 2018'
asctime(tup)                # 本地元组到本地字符串， 'Sun Jun 17 20:45:10 2018'

formate = '%Y-%m-%d %H:%M:%S'
ftime = strftime(formate, tup)      # 元组到指定格式， '2018-06-17 20:45:10'
ptime = strptime(ftime, formate)    # 指定格式到元组
### time.struct_time(tm_year=2018,tm_mon=6,tm_mday=17,tm_hour=20,tm_min=45,tm_sec=10,tm_wday=6,tm_yday=168,tm_isdst=-1)

ctime(secs-3600*10)         # 时间减10时， 'Sun Jun 17 10:45:10 2018'


########################################################################
###  Datetime
########################################################################