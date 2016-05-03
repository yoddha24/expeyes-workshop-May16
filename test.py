# Program to know the voltages and states of 12 channels in expeyes

import numpy as np
import expeyes.eyesj

p=expeyes.eyesj.open()

channel=np.arange(0,12,1)

def voltages():
	for i in channel:
		a=p.get_voltage(i)			
		print "voltage at channel number %d is %f"%(i,a) 
	print "end of voltage readings\n"

def state():
	for i in channel:
		a=p.get_state(i)
		print "state at channel number %d is %d"%(i,a) 
	print "end of states readings\n"

print voltages()
print state()

