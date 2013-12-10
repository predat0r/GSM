import MOD
import SER
import sys

print 'Test UART\r'

SER.set_speed('115200','8N1')

while 1:
MOD.sleep(5)
a = SER.send('TEST\r\n')
print '%d\r' % a