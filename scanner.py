"""
Python Port Scanner 2.0
"""
import socket  # import the socket library
import sys    # import the sys library for System-specific parameters and functions ###


def open_ports(host, port):  # Return Boolean
    try:    # try connecting to host at port and if successful return true if false got to except
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # declare sock variable using AF_INET which sets the
        # IPv4 and SOCK_STREAM sets protocol to TCP
        sock.connect((host, port))  # connects the socket to the declared host and port
    except socket.error:  # throws an exception returns false
        return False
    except socket.gaierror:  # If hostname could not be resolved
        return False
    return True


list_of_ports = [20, 21, 22, 23, 25, 53, 68, 69, 80, 110, 115,
                 119, 123, 135, 137, 138, 139, 143, 161,
                 194, 311, 443, 445, 660, 993, 1023]  # list which holds the ports that are going to be scanned

for ports in list_of_ports:  # for loop which cycles through the ports
    if open_ports(sys.argv[1], ports):
        print("{} is OPEN!".format(ports))  # prints the open ports to the console
