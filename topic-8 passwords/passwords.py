import hashlib
import codecs 
import os
import random

def bytes_to_str(b):
    s = str(codecs.encode(b,"hex"),"utf-8")
    assert type(s) is str
    return s

def str_to_bytes(s):
    b = codecs.decode(bytes(s,"utf-8"),"hex")
    assert type(b) is bytes
    return b

def encode_password(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'),salt,100000)
    salt = bytes_to_str(salt)
    key = bytes_to_str(key)
    return f'{salt}:{key}'

def verify_password(password, encoding):   
    salt, saved_key = encoding.split(':')
    salt = str_to_bytes(salt)
    password_key = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'),salt,100000)
    password_key = bytes_to_str(password_key)
    return saved_key == password_key

if __name__ == "__main__":
    e = encode_password("foobar")
    print(type(e))
    print(e)
    r = verify_password("foobar", e)
    print(r)
    r = verify_password("fxxoobar", e)
    print(r)