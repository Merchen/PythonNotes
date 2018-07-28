import sys
import time
import itertools
import asyncio
import aiohttp

from __futures import clock, DownloadFlags


# asyncio.Future与futures.Future(concurrent)
#
# asyncio.async(coro_future, *, loop=Done)
# coro_future为Future或Task对象时就地返回，否则调用create_task方法包装函数
#
# future为调度执行某物的结果
# asyncio.BaseEventLoop.create_task(...)排定协程返回Task对象(Future的子类)
# 与futures.Executor.submit(...)返回Future对象效果一致
#
# Task对象用于驱动协程, Thread对象用于调用对象
# Task对象一般有asyncio.async()或loop.create_task()返回
#
# asyncio.Future对象通过使用yield from获取结果， yield from将控制权移交给时间循环
# future.add_done_callback(); result = future.result()
# 以上两句组合与result = yield from future等价
#
# asyncio.Future.result()不阻塞协程, 协程未结束时抛出异常
# Task.cancel()可终止任务
#

# 非强制要求, 建议装饰(凸显协程函数)
@asyncio.coroutine
def spin():
    for c in itertools.cycle('|/-\\'):
        status = '\r' + c + ' thinking!'
        sys.stdout.write(status)
        sys.stdout.flush()
        try:
            # 不阻塞事件循环的休眠
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break

@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin())
    yield from asyncio.sleep(2)
    spinner.cancel()
    return True

def __test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(supervisor())
    loop.close()


class asyncDL(DownloadFlags):


    @asyncio.coroutine
    def download(self, country):
        url = '{}/{c}/{c}.gif'.format(self.base_url, c=country.lower())
        resp = yield from aiohttp.ClientSession().get(url)
        image  = yield from resp.read()
        self.save(image, country)
        return country

    @clock
    def execute(self):
        loop = asyncio.get_event_loop()
        to_do = [self.download(cc) for cc in self.countries]
        wait = asyncio.wait(to_do)
        res, _ = loop.run_until_complete(wait)
        loop.close()

# asyncDL().execute()


