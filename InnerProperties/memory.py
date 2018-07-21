
import sys
# 基本数据类型所占内存空间


"""list"""
sys.getsizeof(list())
# 64
sys.getsizeof([1])
# 72
sys.getsizeof([1, 2])
# 80
sys.getsizeof(['DDSFDSF', 'ASDFDS'])
# 80


"""dict"""
sys.getsizeof(dict())
# 240
sys.getsizeof(dict(zip(range(5), range(5))))
# 240
sys.getsizeof(dict(zip(range(6), range(6))))
# 368
sys.getsizeof(dict(zip(range(10), range(10))))
# 368
sys.getsizeof(dict(zip(range(20), range(20))))
# 648


"""int"""
sys.getsizeof(1)
# 28


"""float"""
sys.getsizeof(1.0)
# 24


"""set"""
sys.getsizeof(set())
# 224
sys.getsizeof(set(range(4)))
# 224
sys.getsizeof(set(range(5)))
# 736


"""tuple"""
sys.getsizeof(tuple())
# 48
sys.getsizeof((1, 2))
# 64
sys.getsizeof((1, 2, 3))
# 72
sys.getsizeof((1, 2), (3, 4))
# 64
sys.getsizeof((1, 2, 3), (3, 4))
# 72
