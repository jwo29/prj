import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(255) # 모든 원소에 255(white)

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
