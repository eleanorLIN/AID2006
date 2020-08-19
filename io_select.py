from socket import *
from select import select

sock = socket()
sock.bind(('0.0.0.0',6666))
socket.listen(3)

sock.setblocking(False)
rlist = [sock]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is sock:
            connfd,adr = sock.accept()
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
    for w in ws:
        w.send(b'ok')
        wlist.remove(2)















































