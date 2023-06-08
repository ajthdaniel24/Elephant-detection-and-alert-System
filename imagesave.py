import serial
import io
from PIL import Image
from struct import unpack
from array import array

ser = serial.Serial('COM4', 1000000) # replace with your serial port and baud rate

message = "Yes"
ser.write(message.encode())
print("message sent")

ser.close()

ser = serial.Serial('COM4', 1000000, timeout=1)

# capture frame
ser.write(b'1')
image_data = ser.read(230400)
print("frame captured");

# convert image data to Pillow image object
im = Image.frombytes('L', (320, 240), image_data)

# save image in BMP format
im.save('captured_image.bmp')
print("image saved")

# close serial connection
ser.close()
