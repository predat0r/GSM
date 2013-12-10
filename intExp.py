import MOD
import MDM
import SER

SER.set_speed('115200','8N1')

def ledBlink( count ):
    for _ in range(count):
        GPIO.setIOvalue(7,1)
        MOD.sleep(3)
        GPIO.setIOvalue(7,0)
        MOD.sleep(3)

def checkNetwork():
    MOD.sleep(20)
    REC_TIME = 200
    for _ in range(10):
        MDM.send("AT+CREG?\r",0)
        res = MDM.receive(REC_TIME)
        if (res.find('0,1')!=-1): return 1
        else: MOD.sleep(50)
    return 0

def sendSMS( number, smstext):#, csca):
    if number=="" or smstext=="" : return 0 # or csca == "" : return 0
    #MDM.send('AT+CSCA='+csca+'r',2)
    #MDM.receive(20)
    MDM.send('AT+CMGF=1\r',2)
    MDM.receive(20)
    a = MDM.send('AT+CMGS="' + number + '"\r', 2)
    res = MDM.receive(10)          
    a = MDM.send(smstext, 2)
    a = MDM.sendbyte(0x1A, 2)
    a=''
    while a=='':
        a = MDM.receive(20)
    return ( a.find('OK')!=-1 )

ledBlink(1)
SER.send("Start\r\n")

ledBlink(2)

while not checkNetwork():
    SER.send ("No network\n\r")
    MOD.sleep(10)
SER.send ("I find network\n\r")

ledBlink(3)

myNumber = "+79118468668"
myText = "Hello world"
#smsGate = "+79037011111"
SER.send("Try to send SMS\n\r")
ledBlink(4)
if sendSMS(myNumber,myText):#,smsGate):
    SER.send ("SMS sended\r\n")
else:
    SER.send("SMS not sended\r\n")