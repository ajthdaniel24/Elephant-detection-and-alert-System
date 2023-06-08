import serial

# Open the serial port
ser = serial.Serial('COM4', 9600)

while True:
    # Wait for data from the Arduino
    if ser.in_waiting > 0:
        print('waiting]')
        # Read the data and save it to a file
        with open('audio.wav', 'ab') as f:
            f.write(ser.read(ser.in_waiting))
        
        # Send a confirmation message to the Arduino
        print('saved')
        ser.write(b'OK')
