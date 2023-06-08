import serial
import time

# Open the serial port
ser = serial.Serial('COM4', 1000000) 

# Wait for the Arduino to initialize
time.sleep(2)

# Send a message to the Arduino
message = "No"
ser.write(message.encode())
ser.close()
