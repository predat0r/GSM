import SER
import sys

SER.set_speed('115200','8N1')
class SerWriter:
	def __init__(self):
		SER.set_speed('115200','8N1')

	def write(self,s):
		SER.send(s+'r')
sys.stdout = sys.stderr = SerWriter()

print "SMS sended"