import os
import requests
from concurrent import futures
import time


def clock(fun):
    def decorate(*args, **kwargs):
        t0 = time.time()
        fun(*args, **kwargs)
        print(time.time() - t0)
    return decorate


class DownloadFlags():
    countries = ['CN', 'IN', 'US', 'BR', 'PK', 'NG']
    base_url = 'http://flupy.org/data/flags'
    base_path = os.path.dirname(__file__)

    try:
        # print(os.path.exists('../module'))
        os.makedirs('./flags', exist_ok=False)
    except:
        pass

    def download(self, country):
        url = '{}/{c}/{c}.gif'.format(self.base_url, c=country.lower())
        return requests.get(url).content

    def save(self, image, name):
        path = os.path.join(self.base_path, 'flags/' + name + '.gif')
        with open(path, 'wb') as img:
            img.write(image)

    @clock
    def execute(self):
        for country in self.countries:
            image = self.download(country)
            self.save(image, country)


class _ThreadPoolExecutor1(DownloadFlags):

    @clock
    def execute(self):
        def _(country):
            image = self.download(country)
            self.save(image, country)
        with futures.ThreadPoolExecutor(4) as executor:
            # 使用future对象, 并返回迭代器
            # __next__方法调用future的result方法
            # 返回结果顺序与countries一致, 等待全部完成后返回结果
            executor.map(_, self.countries)


class _ThreadPoolExecutor2(DownloadFlags):

    @clock
    def execute(self):
        def _(country):
            image = self.download(country)
            self.save(image, country)
            return True

        with futures.ThreadPoolExecutor(3) as executor:

            # 此种形式等价于单进程
            # to_do = (executor.submit(_, c) for c in self.countries)
            # [i.result() for i in to_do]

            # 排定对象, 返回future对象列表
            to_do = (executor.submit(_, c) for c in self.countries)
            print(to_do)
            # [<Future at 0xe400d74a20 state=running>,
            # ...3个运行, 3个等待
            # <Future at 0xe400d99f98 state=pending>]

            # as_completed运行结束后返回future对象
            ac = futures.as_completed(to_do)
            for future in ac:
                # future运行结束之后返回result
                print(future.result(),future)
                # True, <Future at 0x438dce9208 state=finished returned NoneType>



