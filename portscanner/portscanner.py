import sys
import socket
from datetime import datetime

# Defines a target
remote_server = input("Enter a remote host to scan: ")
remote_server_ip = socket.gethostbyname(remote_server)

# Print a nice banner with information on which host we are about to scan
print ("-" * 60)
print ("Please wait, scanning remote host", remote_server_ip)
print ("-" * 60)

#get time for when we start scan
tbefore = datetime.now()


try:
    #scans ports from 1 to 65535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((remote_server_ip, port))
        if result == 0:
            print ("Port {}: Open".format(port))
        s.close()
#error handling
except KeyboardInterrupt:
    print("\nExiting the program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

#checking the time when completed
tafter = datetime.now()
#finding how long it took to scan
total = tafter - tbefore

#printing the information
print("Scanning completed in: ", total)
