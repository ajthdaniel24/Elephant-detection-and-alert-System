import serial
import time

# Open the serial port
ser = serial.Serial('COM4', 1000000) 

# Wait for the Arduino to initialize
time.sleep(2)

# Send a message to the Arduino
message = "Yes"
ser.write(message.encode())
ser.close()

while True:
    # Wait for data from the Arduino
    if ser.in_waiting > 0:
        # Read the data and save it to a file
        with open('audio.wav', 'ab') as f:
            f.write(ser.read(ser.in_waiting))
        