#Import necessary packages
import serial
import sys
import time

#Define function to send sms 
def phoneSms():
	
	#Create object for serial communication with the port
	phone = serial.Serial()

	#Setup the port for communication
	phone.port="COM3"
	phone.baudrate=9600
	phone.timeout=9
	phone.xonxoff=False
	phone.rtscts=False
	phone.bytesize=serial.EIGHTBITS
	phone.parity=serial.PARITY_NONE
	phone.stopbits=serial.STOPBITS_ONE
	
	#Opens the port
	phone.open()

	#Checks the connection of GSM module is correct
	phone.write('AT'+'\r\n')
	rcv = phone.read(10)
	print rcv
	time.sleep(1)

	#Disable echoing of commands inorder to reduce confusions while communication
	phone.write('ATE0'+'\r\n')
	rcv = phone.read(10)
	print rcv
	time.sleep(1)

	#Changing the mode of texting to text mode
	phone.write('AT+CMGF=1'+'\r\n')
	rcv = phone.read(10)
	print rcv 
	time.sleep(1)

	#Set new message remind
	phone.write('AT+CNMI=2,1,0,0,0'+'\r\n')   
	rcv = phone.read(10)
	print rcv
	time.sleep(1)

	#Sends SMS to the specified mobile number
	phone.write('AT+CMGS="9447862096"'+'\r\n')
	rcv = phone.read(10)
	print rcv
	time.sleep(1)
	
	#Template of the message content
	phone.write('ACCIDENT Detected near Varikoly'+'\r\n')  
	rcv = phone.read(10)
	print rcv
	 
	#ctrl + z, to send SMS
	phone.write("\x1A") 
	for i in range(10):
		rcv = phone.read(10)
		print rcv