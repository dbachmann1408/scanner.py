"""
Python Port Scanner 2.0
"""
import socket  # import the socket library
import sys    # import the sys library for System-specific parameters and functions ###


def open_ports(host, port):  # Return Boolean
    """
    Creates a socket stream and attempts to connect to a port
    """
    try:    # try connecting to host at port and if successful return true if false got to except
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # declare sock variable using AF_INET which sets the IPv4 and SOCK_STREAM to TCP
        sock.connect((host, port))  # connects the socket to the declared host and port
    except socket.error:  # throws an exception returns false
        return False
    except socket.gaierror:  # If hostname could not be resolved
        return False
    return True


# CONFIG - Lists the ports that will be scanned
LIST_OF_PORTS = [20, 21, 22, 23, 25, 53, 68, 69, 80, 110, 115,
                 119, 123, 135, 137, 138, 139, 143, 161, 194,
                 311, 443, 445, 660, 993, 1023]

for ports in LIST_OF_PORTS:  # for loop which cycles through the ports
    if open_ports(socket.gethostbyname(socket.gethostname()), ports):
        print(socket.gethostbyname(socket.gethostname()) + ": Port {} is OPEN!".format(ports))  # prints the open ports to the console
    else:
        print(socket.gethostbyname(socket.gethostname()) + ": Port {} is not opened".format(ports))
