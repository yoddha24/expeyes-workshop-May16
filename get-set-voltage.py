# Program to check the error in output voltage when PVS is set to a certain value
# Connect PVS to either IN1 (channel number 3) or to A1 (channel number 1)

import numpy as np
import expeyes.eyesj
import matplotlib.pylab as pl

print "The program is being started\n"

channel_number=input("enter the channel number for probing:\n")

p=expeyes.eyesj.open()
NP = 10000
a=np.linspace(0,5, NP)

error_array=np.zeros(NP)
#error_array=np.zeros(NP,3)

for i in range(NP):
	set_value=p.set_voltage(a[i]) # setting particular 'a' volts at PVS
	out_value=p.get_voltage(channel_number) #connect PVS at chosen channel number provided by yourself
	error_value=out_value-set_value
	print set_value, out_value, error_value
	error_array[i] = error_value
	

print error_array
file=np.savetxt('data-error-set-get-IN1.txt',error_array,delimiter=',')
print file

# Plotting the error w.r.t set voltage
pl.plot(a,error_array,'r*')
pl.xlabel('Set Voltage Value (V)')
pl.ylabel('Error (V)')
pl.show()

print "The program has been completed\n"
	
