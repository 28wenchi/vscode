from urllib import request, parse

url = 'http://httpbin.org/post'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}
"""
req = request.Request(url=url, data=data, headers=header, method='POST')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
"""
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=header, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))