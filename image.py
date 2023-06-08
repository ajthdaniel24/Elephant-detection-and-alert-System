import serial
from PIL import Image

# Open serial connection to Arduino
ser = serial.Serial('COM4', 115200, timeout = 60)

# Read image data from serial and store in a bytearray
image_data = bytearray()
while True:
    chunk = ser.read(256)
    if not chunk:
        break
    image_data.extend(chunk)

# Create an Image object from the image data
img = Image.frombytes('RGB', (80, 80), bytes(image_data))

# Save the image to file
img.save('image.jpg')
print(image_data)