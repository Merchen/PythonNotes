# encoding: UTF-8

import zmq, cPickle
from time import sleep
# server
REP_ADDRESS = 'tcp://*:2017'    # 接收请求发送回复
PUB_ADDRESS = 'tcp://*:5556'

# client
REQ_ADDRESS = 'tcp://localhost:2017'    #
SUB_ADDRESS = 'tcp://localhost:5556'


class RpcObject(object):
    """序列化数据"""

    def __init__(self):
        self.usePickle()

    def pack(self, data):
        pass

    def unpack(self,data):
        pass

    def usePickle(self):
        """使用cPickle作为序列化工具"""
        self.pack = cPickle.dumps
        self.unpack = cPickle.loads
        pass


class ZmqServer(RpcObject):
    """zmq服务器"""

    def __init__(self, rep_address=REP_ADDRESS, pub_address=PUB_ADDRESS):
        """Constructor"""
        super(ZmqServer, self).__init__()

        # 启动标志
        self.__active = False

        # zmq接口
        self.__context = zmq.Context()

        # 请求回应socket
        self.__socketREP = self.__context.socket(zmq.REP)
        self.__socketREP.bind(rep_address)

        # 数据广播socket
        self.__socketPUB = self.__context.socket(zmq.PUB)
        self.__socketPUB.bind(pub_address)

    def start(self):
        """启动标志"""
        self.__active = True

    def pub(self, data):
        """发送数据"""
        # 多次发送，客户端来不及接收时，数据写入缓冲区
        pdata = self.pack(data)
        self.__socketPUB.send(pdata)

    def rep(self):
        """响应请求"""
        data = self.__socketREP.recv()
        self.callback(self.unpack(data))

    def callback(self,list_pdata):
        for pdata in list_pdata:
            expression = self.unpack(pdata)
            try:
                res = eval(expression)
                pres = self.pack(res)
            except Exception as err:
                res = 'Occured error:%s' %err
                pres = self.pack(res)
            self.__socketREP.send(pres)

    def run(self):
        if self.__active:
            print('Server Started')
        while self.__active:
            print('Waiting for client request service...')
            pListData = self.__socketREP.recv_multipart()
            print('Received request.')
            self.callback(pListData)


class ZmqClient(RpcObject):
    """zmq客户端"""

    def __init__(self, req_address=REQ_ADDRESS, sub_address=SUB_ADDRESS, filter=''):
        """Constructor"""
        super(ZmqClient, self).__init__()

        # 启动标志
        self.__active = False

        # zmq端口相关
        self.__context = zmq.Context()

        # 请求发出socket
        self.__socketREQ = self.__context.socket(zmq.REQ)
        self.__req_address = req_address

        # 广播订阅socket
        self.__socketSUB = self.__context.socket(zmq.SUB)
        self.__sub_address = sub_address
        # 订阅过滤
        self.__socketSUB.setsockopt(zmq.SUBSCRIBE, filter)

    def start(self):
        # 连接端口
        self.__socketREQ.connect(self.__req_address)
        self.__socketSUB.connect(self.__sub_address)
        self.__active = True

    def sub(self, filter=''):
        """接收数据"""
        data = self.__socketSUB.recv()
        return self.unpack(data)

    def req(self,data):
        pdata = self.pack(data)
        self.__socketREQ.send(pdata)

    def run(self):
        while self.__active:
            inputs = raw_input('>>')
            pdata = self.pack(inputs)
            self.__socketREQ.send(pdata)
            # 等待服务器响应请求
            if not self.__socketREQ.poll(1000):
                continue
            # 接收服务器数据
            pdata = self.__socketREQ.recv()
            data = self.unpack(pdata)
            print(data)


if __name__ == '__main__':

    server = ZmqServer()
    server.start()
    server.run()

    #
    # client = ZmqClient()
    #     # client.start()
    #     # client.run()


    # import numpy
    #
    # array = numpy.array(range(100))
    # new_array = array[0:len(array):2]
