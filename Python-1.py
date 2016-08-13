import netifaces as ni
ip = ni.ifaddresses("wlan0")
print ip  # should print "192.168.100.37"
ip = ni.ifaddresses("wlan0")[2]
print ip
ip = ni.ifaddresses("wlan0")[2][0]
print ip
ip = ni.ifaddresses("wlan0")[2][0]['addr']
print ip