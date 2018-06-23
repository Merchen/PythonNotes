# encoding: UTF-8

"""
打开一个程序就是分配一个进程，每个进程可开启多个线程
进程：独立开辟内存
线程：共享同一进程的变量空间
"""
from Queue import Queue
from collections import defaultdict
from threading import Thread
from time import sleep

EVENT_LOG = 'eLog'
EVENT_TIMER = 'eTimer'


class TestQTimer(object):

    def __init__(self):
        """构造函数"""

        # 存储事件队列
        self.__queue = Queue()

        # 主线程
        self.___threadActive = False
        self.__thread = Thread(target=self.__runThread)

        # 计时器线程
        self.___timerActive = False
        self.__timer = Thread(target=self.__runTimer)

        # 存储事件的回调函数的字典，键名为事件类型，键值为集合包含多个处理方法
        self.__handlers = defaultdict(set)

        # 回调函数保存至字典
        self.register(EVENT_LOG, eventFun1)
        self.register(EVENT_LOG, eventFun2)
        self.register(EVENT_TIMER, eventFun3)

    def __runThread(self):
        """主线程关联方法"""
        while self.___threadActive == True:
            try:
                # 阻塞一秒从队列中获取数据
                event = self.__queue.get(block=True, timeout=3)
                self.__process(event)
            except Exception:
                pass

    def __runTimer(self):
        """计时器关联方法"""
        while self.___timerActive == True:
            evt1, evt2, evt3 = Event(EVENT_LOG), Event(EVENT_LOG), Event(EVENT_TIMER)
            self.__queue.put(evt1)
            # self.__queue.put(evt2)
            self.__queue.put(evt3)
            sleep(2)

    def __process(self, event):
        """事件处理"""
        if event.type_ in self.__handlers.keys():
            [handler(event) for handler in self.__handlers[event.type_]]

    def start(self):
        """启动线程"""
        self.___threadActive = True
        self.__thread.start()

        self.___timerActive = True
        self.__timer.start()

    def register(self, eventType, handler):
        self.__handlers[eventType].add(handler)

    def unregister(self, eventType, handler):
        handlers = self.__handlers
        etype = eventType.type_
        if etype in handlers.keys():
            if handler in  handlers[etype]:
                handlers[etype].remove(handler)
                if not handlers[etype]:
                    del handlers[etype]



class Event(object):
    """事件类"""

    def __init__(self, eventType=None):
        self.type_ = eventType
        self.dict_ = {}


def eventFun1(event): print('eventFun1 Called.')


def eventFun2(event): print('eventFun2 Called.')


def eventFun3(event): print('eventFun3 Called.')


if __name__ == '__main__':
    a = TestQTimer()
    a.start()
