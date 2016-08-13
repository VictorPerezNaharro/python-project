import socket
import subprocess
import tempfile
import os


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip = get_ip_address()

p = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
out, err = p.communicate()
print out