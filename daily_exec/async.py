# coding=utf-8
import socket
import time

#非阻塞方式
def nonblocking_way():
     sock=socket.socket()
     sock.setblocking(False)
     try:
         sock.connect(('example.com',80))
     except BlockingIOError:
         #
         pass
     request='GET/HTTP/1.0\r\nHost:example\r\n\r\n'
     data=request.encode('ascii')
     #
     while True:
         try:
             sock.send(data)
             #
             break
         except OSError:
             pass

     response=b''
     while True:
         try:
             chunk=sock.recv(4096)
             while chunk:
                 response+=chunk
                 chunk=sock.recv(4096)
             break
         except OSError:
             pass
     return response

def sync_way():
    res=[]
    for i in range(10):
        res.append(nonblocking_way())
    return len(res)


#同步阻塞方式


def sync_way():
    res=[]
    for i in range(10):
        res.append(blocking_way())
    return len(res)

#多进程
from concurrent import futures
def blocking_way():
    sock=socket.socket()
    sock.connect(('example.com',80))
    request='GET /HTTP/1.0\r\nHost:example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response=b''
    chunk=sock.recv(4096)
    #sock.connect()和sock.recv()这两个调用在默认情况下是阻塞的
    while chunk:
        response+=chunk
        chunk=sock.recv(4096)
    return response

def process_way():
    workers=10
    with futures.ProcessPoolExecutor(workers) as executor:
        futs={executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])

#多线程
def thread_way():
    workers=10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs={executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])



#epoll结合回调机制
from selectors import DefaultSelector,EVENT_READ,EVENT_WRITE
selector=DefaultSelector()
stopped=False
urls_todo={'/','/1','/2','/3','/4','/5','/6','/7','/8','/9'}

class Crawler:
    def __init__(self,url):
        self.url=url
        self.sock=None
        self.response=b''

    def fetch(self):
        self.sock=socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('example.com',80))
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(),EVENT_WRITE,self.connected)

    def connected(self,key,mask):
        selector.unregister(key.fd)
        get='GET {0} HTTP1.0\r\nHost:example.com\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('ascii'))
        selector.register(key.fd,EVENT_READ,self.read_response)

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

#事件循环
def loop():
    while not stopped:
        #阻塞，直到一个事件发生
        events=selector.select()
        for event_key,event_mask in events:
            callback=event_key.data
            callback(event_key,event_mask)

if __name__ == '__main__':
    start=time.time()
#print(thread_way())
#print(sync_way())
    for url in urls_todo:
        crawler=Crawler(url)
        crawler.fetch()
    loop()
    print(time.time()-start)

