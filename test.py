import MDM
import MOD
import GPIO

answer = ''
i = 0

# Wait network registration
while answer == -1:
    res = MDM.send('AT+CREG?', 0)
    res = MDM.sendbyte(0x0d, 0)
    answer = (MDM.receive(10)).find('0,1')
    res = MOD.sleep(10)

while answer == -1:
    res = MDM.send('AT+COPS?', 0)
    res = MDM.sendbyte(0x0d, 0)
    answer = (MDM.receive(10)).find('MTS RUS')
    res = MOD.sleep(10)

while i != 40:
    res = GPIO.setIOvalue(7,1)
    res = MOD.sleep(3)
    res = GPIO.setIOvalue(7,0)
    res = MOD.sleep(3)
    i = i + 1

i = 0

