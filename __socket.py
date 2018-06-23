# -*- coding: utf-8 -*-

# 套接字
#
# 分叉: 从父进程中复制出子进程，子进程具有内存副本，父子进程并行运行，占用资源较多，windows不支持分叉
# 线程: 轻量级进程（子进程），位于同一进程且共享内存，需解决数据同步问题
#
import socket, select
from urllib import urlopen, urlretrieve
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

HOST = socket.gethostname()
PORT = 1234


def scoket_server():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    # 队列中最大等待接纳数
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print(addr, ' connected.')
        # 向连接客户端发送数据
        client.send('Tank you for connecting')
        client.close()


def socket_client():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    # 接受服务器消息，指定最长字节
    msg = sock.recv(1024)
    print(msg)


def url_open():
    webpage = urlopen('http://news.baidu.com')
    contents = webpage.read()
    print(contents)


URL = 'http://picture.youth.cn/qtdb/201806/W020180617515331718968.jpg'
NEW_NAME = 'retrieve.jpg'


def url_retrive(url=URL, new_name=NEW_NAME):
    urlretrieve(url, new_name)


# 线程化
class Server(ThreadingMixIn, TCPServer): pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from ', addr)
        self.wfile.write('Tank you for connecting')


def threading_server():
    server = Server(('', 1234), Handler)
    server.serve_forever()


# 异步I/O
def asyn_server():
    sock = socket.socket()
    sock.bind((HOST, PORT))
    sock.listen(5)
    inputs = [sock]
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is sock:
                client, addr = sock.accept()
                print('Got connection from ', addr)
                client.send('Tank you for connecting')
                inputs.append(client)
        else:
            try:
                msg = r.recv(1024)
                disconnected = not msg
            except socket.error():
                disconnected = True

            if disconnected:
                print(r.getpeername(), 'disconnected')
                inputs.remove(r)
            else:
                print(msg)