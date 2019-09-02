import urllib.request

#class Request(builtins.object)
#|  Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))