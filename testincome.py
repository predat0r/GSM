import SER
import sys
import MOD
import MDM

TIMEOUT_VALUE = 30
counter = 0
#
#class SerWriter:
#    def __init__(self):
#        SER.set_speed('115200','8N1')
#
#    def write(self,s):
#        SER.send(s+'\r')
#
#sys.stdout = sys.stderr = SerWriter()

SER.set_speed('115200','8N1')
SER.send('+++ START +++\r\n')
#MDM.send('AT+CLIP=1\r',10)
#a = MDM.receive(15)
#SER.send('AT+CLIP=1 - ' + a +'\r\n')
timeout = MOD.secCounter() + TIMEOUT_VALUE

while MOD.secCounter() < timeout:


    #res = SER.read()
    #while (len(res) == 0) and (MOD.secCounter() < timeout):
    #    res = res + SER.read()
    #if res.find('RING') != -1:
    #    print 'I have a call'

    #counter = counter + 1
    #SER.send('Try ' + str(counter) + '\r\n')
    if MDM.getRI() == 1:
        #SER.send('I have a ring\r\n')
        MDM.send('AT+CLCC\r',1)
        md = MDM.receive(10)
        if md.find('9118468668') != -1:
            SER.send('I have a call from you!\r\n')
            MOD.sleep(30)
            MDM.send('ATH\r',0)
        #SER.send('mds = ' + str(mds) + '\r\nmd = ' + str(md) + '\r\n')


SER.send('+++ END +++\r\n')

#RING
#
#+CLIP: "+79118468668",145,"",128,"",0
