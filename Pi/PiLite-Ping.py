import os
import sys
import serial
import time

# Loading Sprite
sprite1 = '000000000000000000000000000000000000111000111100101001100010001100010001100101001111000111000000000000000000000000000000000000'
#  Pass Sprite
sprite2 = '000000000001111100010000010100000001100001001101100101100000101100000101101100101100001001100000001010000010001111100000000000'
# Fail Sprite
sprite3 = '000000000001111100010000010100000001100000101101101001100001001100001001101101001100000101100000001010000010001111100000000000'
# Configure Pi serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/serial0"


def check_ping():
    hostname = "10.8.0.1"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "1"
    else:
        pingstatus = "0"

    return pingstatus

try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    # There was an error
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)

print "Serial port ready"

#Main Loop
while True:
	# Clear display
	print "Clearing Display"
	s.write("$$$ALL,OFF\r")

	# Send Loading Sprite
	print "Loading..."
	s.write('$$$F' + sprite1 + '\r')

	# Run Ping Test
	time.sleep(2)
	if check_ping() == "1":
		print "Ping Was Succsefull!"
		# Send Smile Sprite
		s.write('$$$F' + sprite2 + '\r')
		time.sleep(60)
	else:
		print "Ping Failed!"
		# Send Fail Sprite
		s.write('$$$F' + sprite3 + '\r')
		time.sleep(5)
