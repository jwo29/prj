# 4-11
import numpy as np
import cv2 as cv

olive, violet = (128, 128, 0), (221, 160, 221)

def onChangeThickness(value):
    global thickness
    thickness = 1 if value == 0 else value

def onChangeRadius(value):
    global radius
    radius = 1 if value == 0 else value

def onMouse(event, x, y, flag, param):
    global thickness, radius

    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(image, (x, y), radius, olive, thickness, cv.LINE_AA)
        cv.imshow(title, image)
    elif event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(image, (x-15, y-15, 30, 30), violet, thickness, cv.LINE_AA)
        # cv.rectangle(image, (x-15, y-15, 30, 30), violet, cv.LINE_4)
        cv.imshow(title, image)

title = '4-10'
image = np.zeros((300, 500, 3), np.uint8)
image[:] = (255, 255, 255)

# 초기 선굵기, 반지름 선언
thickness, radius = 1, 20

cv.imshow(title, image)

cv.createTrackbar('Thickness', title, thickness, 10, onChangeThickness) # 선 굵기 최대 10
cv.createTrackbar('radius', title, radius, 50, onChangeRadius) # 반지름 최대 50

cv.setMouseCallback(title, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()
