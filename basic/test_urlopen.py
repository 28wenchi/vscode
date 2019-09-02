import urllib.request
import urllib.parse


#urlopen(url, data=None, timeout=<object object at 0x00564778>, *, cafile=None, capath=None, cadefault=False, context=None)
response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode("utf-8"))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader("Server"))

"""
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response - urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read())
import urllib.parse
import urllib.request
import urllib.error
import socket
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
#response= urllib.request.urlopen('http://httpbin.org/post', data=data)
#@print(response.read())
try:
    response= urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
"""