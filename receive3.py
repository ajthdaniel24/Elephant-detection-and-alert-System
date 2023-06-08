import serial
import os
from PIL import Image
import wave

# set up the serial port (update the port and baudrate as needed)
ser = serial.Serial('COM4', 1000000)

# read data from the serial port
data = ser.readline()

# determine the file type based on file extension
filename = data.decode().strip()  # assuming Arduino sends the filename via serial
extension = os.path.splitext(filename)[1]

if extension in ['.jpg', '.bmp']:
    # if the file is an image, save it to the laptop
    with open(filename, 'wb') as f:
        while True:
            chunk = ser.read(1024)
            if not chunk:
                break
            f.write(chunk)

    # open the image file using the Pillow library
    with Image.open(filename) as img:
        print('Image size:', img.size)
        print('Image format:', img.format)
        
elif extension == '.wav':
    # if the file is audio, save it to the laptop
    with open(filename, 'wb') as f:
        while True:
            chunk = ser.read(1024)
            if not chunk:
                break
            f.write(chunk)
            
    # open the audio file using the wave module
    with wave.open(filename, 'r') as wf:
        print('Channels:', wf.getnchannels())
        print('Sample width:', wf.getsampwidth())
        print('Sampling rate:', wf.getframerate())

else:
    print('File type cannot be determined')

# close the serial port
ser.close()
