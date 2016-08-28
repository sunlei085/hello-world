# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

from wsgi_hello import application

httpd = make_server('', 10000, application)

print('server HTTP on port 10000')

httpd.serve_forever()
