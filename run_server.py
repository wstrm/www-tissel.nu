#!/usr/bin/env python2
import SimpleHTTPServer
import SocketServer

PORT = 8323

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
