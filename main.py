from dcrypt import dcrypt
import sys, time

try:

    hash = input('\n[+] Enter the MD5 hashed password: ')

    dicc = input('\n[+] Enter the dictionary path: ')

    dcpasswd = dcrypt(hash, dicc)

    thePasswd = dcpasswd.completePasswd()

    print('\n[-] Results: {}'.format(thePasswd))

except KeyboardInterrupt:

    print('\n[!] Canceling process...')
    
    time.sleep(1)
    
    sys.exit(0)

