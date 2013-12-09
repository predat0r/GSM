import SER
import SER2

SER.set_speed('115200','8N1')
SER.send('test'+'r')
SER2.set_speed('115200','8N1')
SER2.send('test2'+'r')
print 'test'
SER.send('test1')
SER.sendbyte(0x0d, 0)
SER2.send('test2')
SER2.sendbyte(0x0d, 0)
