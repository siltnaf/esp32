
import usocket as socket  # 引用socket模块

# 响应头
responseHeaders = b'''
HTTP/1.1 200 OK
Content-Type: text/html
Connection: close

'''
# 响应头网页正文内容
content = b'''
Hello World!
'''



def test():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # (重要)设置端口释放后立即就可以被再次使用
    s.bind(socket.getaddrinfo("0.0.0.0", 80)[0][-1])  # 绑定地址
    s.listen(5)  # 开启监听（最大连接数5）


    while True:  # mian()函数中进行死循环，在这里保持监听浏览器请求与对应处理
        client_sock, client_addr = s.accept()  # 接收来自客户端的请求与客户端地址
        print('Client address:', client_addr)

        while True:
            h = client_sock.readline() # 按行读取来自客户端的请求内容
            print(h.decode('utf8'), end='')
            if h == b'' or h == b'\r\n':  # 当读取到空行的时候表示接收到一个完整的请求头
                break

        client_sock.write(responseHeaders) # 向客户端发送响应头
        client_sock.write(content) # 向客户端发送网页内容
        client_sock.close()


