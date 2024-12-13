"""cryptology

algorithums

symetric - AES(advanced encryption standard) and DES(data encryption standard)
1 key for encrypting and decrypting

asymetric - RSA
2 keys 1 for encrypting 1 for decrypting

"""

#how to make a safe password

import string
import secrets

def make_password(length=12):
    alfa=string.ascii_letters+string.digits+string.punctuation
    pass2=''.join(secrets.choice(alfa) for i in range(length))
    return pass2


pass2=make_password(16)
print("a good word pass could possibly be this thing right here",pass2)


import uuid

passw=uuid.uuid4()
print(passw)


#use the time in the password - timestamp

import time
import random


hour=time.time() #since 1970 jan 1st (unix time)
print(hour)

pass1=f"{time.time()*1000}-{random.randint(10000,99999)}"
print(pass1)

"""
self evaluation thats just a test

1generēt +-
2cēzar -
3choice +
4+
5secret +
6zīmju dauzdums
7sargāt
8asymetric
9ar zīmēm
10mazāka iespeja rezēs


"""