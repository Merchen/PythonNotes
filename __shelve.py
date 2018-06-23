# -*- coding: utf-8 -*-

########################################################################
###  shelve
########################################################################
#
# 可像普通字典一样访问数据，键名必须为字符串

import shelve

_DBFILE = r'__shelve.dat'

_PERSON1 = {'id': 101,'name': 'Gumby','age': 23,'gender': 'male'}
_PERSON2 = {'id': 203,'name': 'Jorn','location': 'Shanghai','career': 'programmer'}

def test_shelve():
    """
    shelve读写文件测试
    """
    db = shelve.open(_DBFILE)
    try:
        pid = lambda x: str(x['id'])

        db[pid(_PERSON1)] = _PERSON1
        db[pid(_PERSON2)] = _PERSON2

        # 更新数据
        db.sync()

        # 打印数据
        for key, value in db.items():
            print('%s:%s' % (key, value))

    except Exception as err:
        raise 'Error occurred: %s' % err

    finally:
        db.close()

if __name__ == '__main__':
    # test_shelve()
    # ContractData.vt
    db = shelve.open('ContractData.vt')
    try:
        data = db['data']
    except:
        raise
    else:
        import pprint
        pprint.pprint(data.values())
