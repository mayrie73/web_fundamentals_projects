salt = '123' #where the value 123 changes randomly
hashed_password = md5(password + salt)
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
