import socket
from subprocess import Popen, PIPE, STDOUT

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip = get_ip_address()

p = Popen('echo hola', stdout = PIPE, 
        stderr = STDOUT, shell = True)
for line in p.stdout:
    print line.replace('\n', '')