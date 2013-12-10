import MOD
import SER
import GPIO
import sys

SER.set_speed('115200','8N1')
#GPIO.setIOvalue(7,1)
i = 0

def ledBlink( count ):
    for _ in range(count):
        GPIO.setIOvalue(7,1)
        MOD.sleep(2)
        GPIO.setIOvalue(7,0)
        MOD.sleep(2)

class SerWriter:
    def __init__(self):
        SER.set_speed('115200','8N1')

    def write(self,s):
        SER.send(s+'\r')

sys.stdout = sys.stderr = SerWriter()

ledBlink(3)

print 'Test UART\r'

while 1:
    ledBlink(i)
    MOD.sleep(3)
    a = SER.send('TEST ' +str(i) + ' ')
#    print i
    print a
    i = i + 1
    MOD.sleep(3)
    if i>9:
        i=1
