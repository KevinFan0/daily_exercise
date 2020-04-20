# coding=utf-8
#协程
#未来对象 先设计一个对象，异步调用执行完的时候，就把结果放在它里面。这种对象称之为未来对象
import socket
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE

selector=DefaultSelector()
stopped=False
urls_todo={'/','/1','/2','/3','/4','/5','/6','/7','/8','/9'}

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

#重构Crawler
class Crawler:
    def __init__(self,url):
        self.url=url
        self.response=b''

    def fetch(self):
        sock=socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('example.com',80))
        except BlockingIOError:
            pass
        f=Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(),EVENT_WRITE,on_connected)
        yield f
        selector.unregister(sock.fileno())
        get='GET {0} HTTP1.0\r\nHost:example.com\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))

    def read_response(self,key,mask):
        global stopped
        #如果响应大于4KB，下一次循环会继续读
        chunk=self.sock.recv(4096)
        if chunk:
            self.response+=chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped=True


