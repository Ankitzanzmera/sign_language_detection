import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['Hello','Yes','No',"Thanks","I_love_You","Please"]

num_of_images = 20

for label in labels:
    img_path = os.path.join(IMAGE_PATH,label)
    os.makedirs(img_path,exist_ok=True)
    capture = cv2.VideoCapture(0)

    print(f'Collecting Image for {label}')
    time.sleep(5)
    for imgnum in range(num_of_images):
        ret, frame = capture.read()
            # ret =   The first value is a Boolean flag indicating whether the frame was successfully read or not.
            # frame = The second value is the actual frame that was captured.

        imagename = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) &  0xFF==ord('q'):
            break
    capture.release()
