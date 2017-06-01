#!/usr/bin/python
import os
import sys
import glob
import time

import dlib
import cv2

if len(sys.argv) != 2:
    exit()
faces_folder = sys.argv[1]

detector = dlib.simple_object_detector("detector.svm")

#win_det = dlib.image_window()
#win_det.set_image(detector)

print("Showing detections on the images in the faces folder...")
for f in glob.glob(os.path.join(faces_folder, "*.jpg")):
    print("Processing file: {}".format(f))
    img = cv2.imread(f)
   # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(img)
    print("Number of faces detected: {}".format(len(dets)))

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
    
    cv2.imshow("Result", img)
    if cv2.waitKey(0) == 27:
    	break;

cv2.destroyAllWindows()
