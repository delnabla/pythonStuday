#!/usr/bin/env python3
# -*- encodng: utf-8 -*- 

import urllib.request

url="http://www.baidu.com"
data=urllib.request.urlopen(url).read()
data=data.decode('UTF-8')
print(data)
