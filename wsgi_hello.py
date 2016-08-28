# -*- coding: utf-8 -*-

def application(environ, start_response):
    # start_response：发送http响应的函数， 用于wsgi发送http响应信息的header与code。该函数接收两个参数第一个参数是http的响应码
    # 第二个参数是一组list表示的http的header，每个header是一个str组成的tuple。这个application封装了底层的socket通信,使用起来非常方便
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'<h1>Hello, web!</h1>']
