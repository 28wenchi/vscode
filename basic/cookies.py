import http.cookiejar, urllib.request

"""
icookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name+'='+item.value)
"""


filename = 'cookies.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
