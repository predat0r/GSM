import MDM
import MOD
import GPIO

answer = ''

def led_blink( count ): #debug function
    for _ in range(count):
        GPIO.setIOvalue(7,1)
        MOD.sleep(3)
        GPIO.setIOvalue(7,0)
        MOD.sleep(3)

led_blink(2)

# Wait network registration
while answer == -1:
    MDM.send('AT+CREG?\r', 0)
    answer = (MDM.receive(10)).find('0,1')
    MOD.sleep(10)

while answer == -1:
    MDM.send('AT+COPS?\r', 0)
    answer = (MDM.receive(10)).find('MTS RUS')
    MOD.sleep(10)

led_blink(4)

MDM.send('AT+FCLASS=8\r', 0)

while answer == -1:
    MDM.send('ATD +79118468668\r', 0)
    answer = (MDM.receive(200)).find('OK')
    MOD.sleep(30)
    MDM.send('ATH\r', 0)


MDM.send('ATH\r', 0)

led_blink(6)
