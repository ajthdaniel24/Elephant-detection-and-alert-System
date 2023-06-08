import os
import time
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import datetime

fpath = 'C:\\out'

while True:
    # Get a list of all files in the folder
    files = os.listdir(fpath)
    file_count = len([f for f in os.listdir(fpath) if os.path.isfile(os.path.join(fpath, f))])

    if file_count >= 6:
        np.set_printoptions(suppress=True)
        model = load_model('./lastmodel.h5', compile=False)
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open('C:\\out/5.bmp').convert("RGB")

        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        image_array = np.asarray(image)

        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        data[0] = normalized_image_array

        prediction = model.predict(data)
        index = np.argmax(prediction)
        confidence_score = prediction[0][index]

        if index == 0:
            brO = "{ "
            status = "status: true"
            ti = " time:"
            time = datetime.datetime.now().time()
            da = " date:"
            date = datetime.datetime.now().strftime("%m/%d/%Y")
            brC = " }"
            final = brO + status + ti + str(time) + da + str(date) + brC
            print(final)
        else:
            brO = "{ "
            status = "status: false"
            ti = " time:"
            time = datetime.datetime.now().time()
            da = " date:"
            date = datetime.datetime.now().strftime("%m/%d/%Y")
            brC = " }"
            final = brO + status + ti + str(time) + da + date + str(date) + brC
            print(final)

        # Loop through each file and delete it
        for file_name in files:
            # Construct the full file path by joining the folder path and file name
            file_path = os.path.join(fpath, file_name)
            # Check if the file is a file (not a directory)
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)
        break
    else:
        time.sleep(3)