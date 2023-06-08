import serial

ser = serial.Serial('COM4', 1000000)
while True:
    data = ser.read()
    print('reading')
    if data == b'\x42':  # BMP file header
        data = ser.read(3)
        size = (data[0] << 16) | (data[1] << 8) | data[2]
        bmp_data = ser.read(size)
        with open('image.bmp', 'wb') as f:
            f.write(b'\x42')
            f.write(size.to_bytes(3, 'big'))
            f.write(bmp_data)
            print("image saved")
    elif data == b'\x52':  # WAV file header
        print("audio file found")
        data = ser.read(3)
        size = (data[0] << 16) | (data[1] << 8) | data[2]
        wav_data = ser.read(size)
        with open('audio.wav', 'wb') as f:
            f.write(b'\x52')
            f.write(size.to_bytes(3, 'big'))
            f.write(wav_data)
            print("audio saved")