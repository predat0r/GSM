import SER
import sys


class SerWriter:
    def __init__(self):
        SER.set_speed('115200','8N1')

    def write(self,s):
        SER.send(s+'\r')

sys.stdout = sys.stderr = SerWriter()

print 'START'

print 'END'