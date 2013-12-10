import MDM
import MOD
import GPIO
import sys
import SER


def led_blink( count ): #debug function
    for _ in range(count):
        GPIO.setIOvalue(7,1)
        MOD.sleep(3)
        GPIO.setIOvalue(7,0)
        MOD.sleep(3)

class SerWriter:
    def __init__(self):
        SER.set_speed('115200','8N1')

    def write(self,s):
        SER.send(s+'\r')

sys.stdout = sys.stderr = SerWriter()

def check_network():
    MOD.sleep(20)
    for _ in range(10):
        MDM.send("AT+CREG?\r",0)
        res = MDM.receive(200)
        print 'check registration'
        if res.find('0,1') != -1:
            print 'registration ok'
            return 1
        else: MOD.sleep(50)
    return 0

print 'Script started'
led_blink(2)

while not check_network():
    print "No network"
    MOD.sleep(10)
print "I find network"

led_blink(4)

MDM.send('AT+FCLASS=8\r', 0)

call_status = 0
while call_status == 0:
    print 'Calling...'
    MDM.send('ATD +79118468668\r', 0)
    print 'Wait modem answer'
    for a in range(10):
        acall = MDM.receive(100)
        print acall
        if acall.find('OK') != -1:
            print 'Answer OK'
            call_status = 1
            MOD.sleep(50)
            break #change for return
        else:
            print 'Wait answer' + str(a)
            MOD.sleep(30)


print 'Terminate call'
MDM.send('ATH\r', 0)

print 'Initialization done'
led_blink(6)
