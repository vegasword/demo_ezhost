import os
import socket
import platform
import urllib.request

def leak():
    print("System Information:")
    print("OS: ", platform.system())
    print("Release: ", platform.release())
    print("Version: ", platform.version())
    print("Machine: ", platform.machine())

    print("\nPublic Network IP:")
    try:
        response = urllib.request.urlopen('https://api.ipify.org')
        ip = response.read().decode('utf8')
        print(ip)
    except Exception as e:
        print("Error: Unable to retrieve public network IP")
        
    print("\nOther Data:")
    print("Hostname: ", socket.gethostname())
    print("Kernel: ", os.uname().sysname)
    print("Home Directory: ", os.path.expanduser("~"))
    print("Current Working Directory: ", os.getcwd())
    print("List of Installed Packages: ", os.popen("dpkg --list").read())

if __name__ == "__main__":
    leak()
