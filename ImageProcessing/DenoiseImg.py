import cv2
import numpy as np

def denoiseImg(img):
    kernel = np.ones((5, 5), np.uint8)

    blurred_img = cv2.GaussianBlur(img,(7,7),0)
    img_erosion = cv2.erode(img, kernel, iterations=2)
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=2)

    return img_dilation