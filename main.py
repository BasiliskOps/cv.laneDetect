import sys
import numpy as np
import cv2

cap = cv2.VideoCapture('/Users/basilisk/Data_Science/Capstone/cv.laneDetect/driving_frame.mp4')

if (cap.isOpened() == False):
    print("Video stream failed to initialize")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('The North Remembers', frame)