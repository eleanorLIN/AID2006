from socket import *
s = socket()
s.bind(("0.0.0.0",8000))
s.listen(3)
c,addr = s.accept()
data = c.recv(1024*10)
print(data.decode())

html =  'HTTP/1.1 200 OK\r\n'
html +='Content-Type:text/html\r\n'
html +='\r\n'
# with open("python.html") as f:
#     html += f.read()
html +='this is a http test.'
c.send(html.encode())
c.close()
s.close()