from urllib import request
from urllib import parse
import http.cookiejar

cookfile = 'cookies.txt'
cookie = http.cookiejar.LWPCookieJar(cookfile)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print(item.name + ' = ' + item.value)

with open('out.html', 'w', encoding='utf-8') as outfile:
    outfile.write(response.read().decode('utf-8'))