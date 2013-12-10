import GPIO
import MOD

i = 0

while i < 100:
    GPIO.setIOvalue(7, 1)
    MOD.sleep(10)
    GPIO.setIOvalue(7, 0)
    MOD.sleep(10)
    i = i + 1