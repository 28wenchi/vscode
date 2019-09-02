# python

## 爬虫基础
    URI : Uniform Resource Identifier 统一资源标志符
    URL : UNiversal Resouce Locator 统一资源定位符
    URL 是 URI 的子集

### way of get
    GET			请求页面，并返回页面内容
    HEAD		类似于 GET 请求， 只不过返回的响应中没有具体的内容，用于获取报头
    POST		大多用于提交表单或上传文件，数据包含在请求体中
    PUT			从客户端向服务器传送的数据取代指定文梢中的内容
    DELETE		请求服务器删除指定的页面
    CONNECT		把服务器当作跳板，让服务器代替客户端防问其他网页
    OPTIONS		允许客户端查看服务器的性能
    TRACE		因显服务器收到的请求，主要用于测试或诊断
    
    Accept ：			请求报头域，用于指定客户端可接受哪些类型的信息 。
    Accept-Language ：	指定客户端可接受的语言类型 。
    Accept-Encoding ：	指定客户端可接受的内容编码 。
    Host ：				用于指定请求资源的主机 IP 和端口号，其内容为请求 URL 的原始服务器或网关的位置。 从 HTTP 1. l 版本开始，请求必须包含此内容。
    Cookie ：			也常用复数形式 Cookies ，这是网站为了辨别用户进行会话跟踪而存储在用户本地的数据 。 它的主要功能是维持当前访问会话 。 例如，我们输入用户名和密码成功登录某个网
    站后，服务器会用会话保存登录状态信息，后面我们每次刷新或请求该站点的其他页面时，会发现都是登录状态，这就是 Cookies 的功劳 。 Cookies 里有信息标识了我们所对应的服务器的会话，每次浏览器在请求该站点的页面时，都会在请求头中加上 Cookies 并将其发送给服务器，服务器通过 Cookies 识别出是我们自己，并且查出当前状态是登录状态，所以返回结
    果就是登录之后才能看到的网页内容 。
    Referer ：			此内容用来标识这个请求是从哪个页面发过来的，服务器可以拿到这一信息并做相应的处理，如做来源统计、防盗链处理等 。
    User-Agent ：		简称 UA,它是一个特殊的字符串头，可以使服务器识别客户使用的操作系统及版本 、 浏览器及版本等信息 。 在做爬虫时加上此信息，可以伪装为浏览器；如果不加，很
    可能会被识别州为爬虫 。
    Content-Type ：		也叫互联网媒体类型（ Internet Media Type ）或者 MIME 类型，在 HTTP 协议,消息头中，它用来表示具体请求中的媒体类型信息.例如text/html 代表 HTML 格式，image/gif代表 GIF 图片， app lication/jso n 代表 JSON 类型，更多对应关系可以查看此对照表 ：http://tool.oschina.neνcommons 。
    
    > Request Headers 中指定content-Type 为application/x-www.form-urllencoded.只有设置content-Type 为application/x-www-form-urlencoded, 才会以表彰数据的形式提交 
    
    application/x-www-forrn-urlencoded	表单数据
    multipart/form-data					表单文件上传
    application/json					序列化 JSON 数据
    text/xmlXML 						数据



## urlopen()

``` 
import urllib.request
rep = urllib.request.rulopen('http://www.python.org')
print(rep.read().decode('utf-8'))
print(type(rep))
<class ’ http.client.HTTPResponse ’ >
```

## parse url

```
urlparse	url的识别和分段
urllib.parese.urlparse(urlstring, scheme='', allow_fragments=True)

urlunparse()	urlsplit()	urlunsplit()	urljoin()	

urlencode()	序列化
parse_qs()	反序列化	return dict
parse_qsl()	反序列化	retuen list config from tuple

quote()		url 编码
unquote		


```

### request

```
r = requests.post(' http://httpbin.org/post ’)
r = requests.put('http : //httpbi 「i. org/put ’)
r = requests .delete( ' http://httpbin.org/delete ' )
r = requests .head(’ http://httpbin .org/get ’)
r = requests.options(’ http://httpbin.org/get')

import requests
r = request.get('http://www.jianshu.com')
exit() if not r.status_code == request.codes.ok else print('Request Successfully')
网页的返回类型实际上是 str 类型，但是它很特殊，是 JSON 格式的 。 所以，如果想直接
解析返回结果，得到一个字典格式的话，可以直接调用 json()方法

r = requests . post(” http ://httpbin .org/post”, files=files)
```

