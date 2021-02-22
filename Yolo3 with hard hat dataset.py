
"""

!sudo ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg

!sudo ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny_final.weights data/1.jpg

from google.colab import drive
drive.mount('/content/drive')

!cd /content/drive/My Drive

!sudo ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny_final.weights data/2.jpg -dont_show

!sudo ./darknet detector demo Hardhat/hardhat.data Hardhat/yolov3-tiny.cfg yolov3-tiny_final.weights Hardhat/engine4.mp4 -out_filename Hardhat/result2.avi -dont_show -thresh 0.05

import cv2