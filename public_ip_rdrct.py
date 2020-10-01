# this runs  on the server side

import http.server
import socketserver

def get_public_ip():
    try:
        f = open('./my_public_ip.txt', encoding = 'utf-8')
        fread = f.read()
    finally:
        if f:
             f.close()
        return(fread)


class FakeRedirect(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        new_ip = get_public_ip()
        self.send_response(301)
        new_path = 'http://%s:1880%s'%(new_ip, self.path)
        self.send_header('Location', new_path)
        self.end_headers()
        return

socketserver.TCPServer(("", 8080), FakeRedirect).serve_forever()