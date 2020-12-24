import subprocess as sp
import docker,  webserver, lvm, hadoop
print("Welcome to Our TUI program")
print("""Select from following options
Press 1 for Docker
Press 2 for Webserver
Press 3 for Hadoop Setup
Press 4 LVM """)
choice = int(input())
if choice == 1:
    docker.docker()
elif choice == 2:
    webserver.webserver()
elif choice == 3:
    hadoop.hadoop()
elif choice == 4:
    lvm.lvm()