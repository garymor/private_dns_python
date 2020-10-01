                                                                   File: publicip_rewrite.py                                                                                


import http.server
import socketserver
from urllib.parse import urlparse

def rewrite_public_ip(o):
    try:
        print(o)
        f = open('./my_public_ip.txt', 'r')
        fread = f.read()
        if o != fread:
            f = open('./my_public_ip.txt', 'w')
            f.write(o)
            print('ip has been updated')
    finally:
        print('finished')


class Requesthandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        o = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        rewrite_public_ip(o.path[1:])
        return


socketserver.TCPServer(("", 8080), Requesthandler).serve_forever()


