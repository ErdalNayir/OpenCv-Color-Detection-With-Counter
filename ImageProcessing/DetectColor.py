import cv2
import numpy as np

def detectColor(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower = np.array([hMin, sMin, vMin])
    # upper = np.array([hMax, sMax, vMax])

    # Defining lower and upper bound HSV values
    lower = np.array([81, 90, 109])
    upper = np.array([103, 255, 255])

    # Defining mask for detecting color
    mask = cv2.inRange(hsv, lower, upper)

    return mask