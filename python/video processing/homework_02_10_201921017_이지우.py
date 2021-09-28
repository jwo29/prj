# 4-10
import numpy as np
import cv2 as cv

olive, violet = (128, 128, 0), (221, 160, 221)

def onMouse(event, x, y, flag, param):
    if event == cv.EVENT_RBUTTONDOWN:
        cv.circle(image, (x, y), 20, olive, 2, cv.LINE_AA)
        cv.imshow(title, image)
    elif event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(image, (x-15, y-15, 30, 30), violet, 2, cv.LINE_AA)
        cv.imshow(title, image)

title = '4-10'
image = np.zeros((300, 500, 3), np.uint8)
image[:] = (255, 255, 255)

cv.imshow(title, image)
cv.setMouseCallback(title, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()