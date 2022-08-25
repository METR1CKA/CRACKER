import hashlib

class dcrypt:

    def __init__(self, passHash, passDicc):
        self.encontrada = 0
        self.passHash = passHash
        self.passDicc = passDicc

    def completePasswd(self):
        try:
            pass_file = open(self.passDicc, 'r')

            password = self.readingAndUnhashingPassword(pass_file)

            if password == False:
                return 'Password not found'

            else:
                return password

        except Exception as e:
            return e

    def readingAndUnhashingPassword(self, pass_file):
        for word in pass_file:
            cipher_word = word.encode('utf-8')

            hashed_word = hashlib.md5(cipher_word.strip())

            digest = hashed_word.hexdigest()

            if digest == self.passHash:
                self.encontrada = 1

                return word

        if not self.encontrada:
            return False

