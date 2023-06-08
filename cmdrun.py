import subprocess
import os
import time
import psutil
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import datetime
import glob
import json

directory = r"C:\Program Files (x86)\Java\jdk1.8.0_74\bin"

command = "java code.SimpleRead"

process = subprocess.Popen(command, shell=True, cwd=directory, stdout=subprocess.PIPE)

try:
    # Wait for the process to complete or raise a TimeoutExpired exception after 60 seconds
    stdout, stderr = process.communicate(timeout=60)
except subprocess.TimeoutExpired:
    # Kill the parent process and all its children
    parent_pid = process.pid
    parent = psutil.Process(parent_pid)
    for child in parent.children(recursive=True):
        child.kill()
    parent.kill()
    print("Process terminated due to timeout")

# Wait for the process to exit and print its return code
return_code = process.wait()

	
fpath = 'C:\\out'
extensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp"] 
files = os.listdir(fpath)

for extension in extensions:
    image_path = glob.glob(os.path.join(fpath, extension))
    if len(image_path) > 0:
        # Found an image with this extension, return its path
        np.set_printoptions(suppress=True)
        model = load_model('./keras_model.h5', compile=False)
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open('C:\\out/1.bmp').convert("RGB")

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        data[0] = normalized_image_array

        prediction = model.predict(data)
        index = np.argmax(prediction)
        confidence_score = prediction[0][index]

        if index == 0:
            z = {
                "status": True,
            }
            y = json.dumps(z)
            print(y)
        else:
            z = {
                "status": False,
            }
            y = json.dumps(z)
            print(y)

        # Loop through each file and delete it
        for file_name in files:
            # Construct the full file path by joining the folder path and file name
            file_path = os.path.join(fpath, file_name)
            # Check if the file is a file (not a directory)
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)
        break
		