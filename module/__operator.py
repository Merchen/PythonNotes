# -*- coding: utf-8 -*-
from operator import attrgetter, itemgetter
from collections import namedtuple


#=======================================================================
"""itemgetter"""
def fun1():
    metro_data = [('Tokyo', 'JP', 36.933),
                  ('Mexico City', 'MX', 20.142),
                  ('Sao Paulo', 'BR', 19.649)]

    # 根据元组的某个字段排序
    cities = [city[:2] for city in sorted(metro_data, key=itemgetter(1))]
    # [('Sao Paulo', 'BR'), ('Tokyo', 'JP'), ('Mexico City', 'MX')]

    cities = [city[:2] for city in sorted(metro_data, key=lambda x:x[1])]
    # [('Sao Paulo', 'BR'), ('Tokyo', 'JP'), ('Mexico City', 'MX')]

    # 构建函数提取元组数值
    cities = [itemgetter(1, 0)(city) for city in metro_data]
    # [('JP', 'Tokyo'), ('MX', 'Mexico City'), ('BR', 'Sao Paulo')]

    cities = list(map(lambda x:(x[1], x[0]), metro_data))
    # [('JP', 'Tokyo'), ('MX', 'Mexico City'), ('BR', 'Sao Paulo')]


#=======================================================================
"""attrgetter"""
def fun2():
    metro_data = [('Tokyo', 'JP', (36.933, 139.671)),
                  ('Mexico City', 'MX', (20.142, 77.554)),
                  ('Sao Paulo', 'BR', (19.649, 45.254))]

    LatLong = namedtuple('latLong', 'lat long')
    Metro = namedtuple('metro', 'name cc coord')

    metro_areas = [Metro(name, cc, LatLong(lat, long)) for name, cc, (lat, long) in metro_data]

    print(metro_areas[1])
    # metro(name='Mexico City', cc='MX', coord=latLong(lat=20.142, long=77.554))

    cities = [city[:2] for city in sorted(metro_areas, key=attrgetter('coord.lat'))]
    # [('Sao Paulo', 'BR'), ('Mexico City', 'MX'), ('Tokyo', 'JP')]