#!/usr/bin/env python

import socket

ip = socket.gethostbyname(socket.gethostname())
sys.stdout.write(ip);