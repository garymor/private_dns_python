
import http.server
import socketserver
from urllib.parse import urlparse
import urllib.request

def main():
    localip = publicip_LocalFile()
    actualip = publicip_actual()
    if localip != actualip :
        update_dnsPublicIp(actualip)



def publicip_LocalFile():
    try:
        f = open('./my_public_ip.txt')
        fread = f.read()
    finally:
        if f:
             f.close()
        return(fread.strip())

def publicip_actual():
    f = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return f.strip()



def update_dnsPublicIp(ip):
    f = open('./my_public_ip.txt', 'w')
    f.write(ip)
    urllib.request.urlopen('http://207.154.233.97:8080/%s' %ip )


main()

