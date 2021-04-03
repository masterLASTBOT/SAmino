from time import time
from uuid import UUID
from os import urandom
from binascii import hexlify


def timestamp():
    return int(time() * 1000)


def uid():
    uuid = str(UUID(hexlify(urandom(16)).decode('ascii')))
    return uuid
