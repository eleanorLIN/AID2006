from socket import *
from select import *
sockfd = socket()
sockfd.bind(('0.0.0.0',6666))
sockfd.listen()
sockfd.setblocking(False)


ep = epoll()
map = dict({})
ep.register(sockfd,EPOLLIN)
map[sockfd.fileno()] = sockfd

while True:
    events = ep.poll()
    for fd,event in events:
        if fd ==sockfd.fileno():
            connfd,addr = map[fd].accept()
            connfd.setblocking(False)
            ep.register(connfd,POLLIN)
            map[connfd.fileno()] = connfd
        elif event==EPOLLIN:
            data = map[fd].recv(1024)
            if not data:
                ep.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print(data.decode())