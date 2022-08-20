from dcrypt import dcrypt
import sys, time

try:

    hash = input('\nEnter the MD5 hashed password: ')

    dicc = input('\nEnter the dictionary path: ')

    dcpasswd = dcrypt(hash, dicc)

    thePasswd = dcpasswd.completePasswd()

    print('\nResults: {}'.format(thePasswd))

except KeyboardInterrupt:

    print('\nCanceling process...')
    
    time.sleep(1)
    
    sys.exit(0)

