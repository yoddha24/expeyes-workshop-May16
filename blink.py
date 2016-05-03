#Program to blink LED (ON=2sec,OFF=2sec)

import expeyes.eyesj
import time

p=expeyes.eyesj.open()

def blink():
	p.set_state(10,1)
	time.sleep(1)
	a1=p.get_state(10)
	print "State of channel 10 is %d"%a1
	a2=p.get_voltage(10)
	print "Voltage at channel number 10 is %f"%a2
	p.set_state(10,0)
	time.sleep(1)
	b1=p.get_state(10)
	print "State of channel 10 is %d"%b1
	b2=p.get_voltage(10)
	print "Voltage at channel number 10 is %f"%b2

print "start of blinking program "
print "**************"

i=0
while i<3:# LED will blink 3 times
	blink()
	i=i+1
	print "LED blink number %d"%i
	
print "LED blinked %d number of times"%i
print "End of blinking program"
print "**************"

