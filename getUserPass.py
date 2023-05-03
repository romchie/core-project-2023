import os
from getpass import getpass

def main():
    u = input("Enter your PODS username: ")
    p = getpass("Enter your PODS password: ")
    os.system("touch .credentials")
    f = open(".credentials", 'w')
    f.write(str(u + '\n' + p + '\n'))
    f.close()

main()