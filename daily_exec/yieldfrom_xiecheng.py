#用yield from 改进生成器协程
#gen_one和gen_two是等价的
def gen_one():
    subgen=range(10)
    yield from subgen
def gen_two():
    subgen=range(10)
    for item in subgen:
        yield item

#子生成器和原生成器的调用者之间打开双向通道，两者可以直接通信。
def gen():
    yield from subgen()
def subgen():
    while True:
        x=yield
        yield x+1
def main():
    g=gen()
    next(g)
    retval=g.send(1)
    print(retval)
    g.throw(StopIteration)

#抽象socket连接的功能
import socket
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE

selector=DefaultSelector()
stopped=False
urls_todo={'/','/1','/2','/3','/4','/5','/6','/7','/8','/9'}

#需要把future改造成一个iterable对象
class Future:
    def __init__(self):
        self.result=None
        self._callbacks=[]

    def add_done_callback(self,fn):
        self._callbacks.append(fn)

    def set_result(self,result):
        self.result=result
        for fn in self._callbacks:
            fn(self)
    def __iter__(self):
        yield self
        return self.result

def connect(sock,address):
    f=Future()
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    def on_connected():
        f.set_result(None)

    selector.register(sock.fileno(),EVENT_WRITE,on_connected())
    yield from f
    selector.unregister(sock.fileno)

#抽象单次recv()和读取完整的response功能
def read(sock):
    f=Future()

    def on_readable():
        f.set_result(sock.recv(4096))

    selector.register(sock.fileno(),EVENT_READ,on_readable)
    chunk=yield from f
    selector.unregister(sock.fileno())
    return chunk

def read_all(sock):
    response=[]
    chunk=yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk=yield from read(sock)
    return b''.join(response)

#重构Crawler
class Crawler:
    def __init__(self,url):
        self.url=url
        self.response='b'

    def fetch(self):
        global stopped
        sock=socket.socket()
        yield from connect(sock,('example.com',80))
        get = 'GET {0} HTTP1.0\r\nHost:example.com\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))
        self.response=yield from read_all(sock)
        urls_todo.remove(self.url)
        if not urls_todo:
            stopped=True