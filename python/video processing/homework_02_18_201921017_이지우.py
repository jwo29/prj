# 4-18
import numpy as np
import cv2 as cv

white, blue, red = (255, 255, 255), (255, 0, 0), (0, 0, 255)

title = '4-18'
image = np.full((400, 600, 3), white, np.uint8)

center = (image.shape[1]//2, image.shape[0]//2) # 이미지의 정중앙 좌표

## 태극 문양 그리기
bigSemiCircleSize = (image.shape[0]//4, image.shape[0]//4) # 큰 타원의 반지름은 높이의 1/4
cv.ellipse(image, center, bigSemiCircleSize, 0, 180, 360, red, cv.FILLED)
cv.ellipse(image, center, bigSemiCircleSize, 0, 0, 180, blue, cv.FILLED)

smallSemiCircleSize = (image.shape[0]//8, image.shape[0]//8) # 작은 타원의 반지름은 높이의 1/8
cv.ellipse(image, (center[0]-image.shape[0]//8, image.shape[0]//2), smallSemiCircleSize, 0, 0, 180, red, cv.FILLED)
cv.ellipse(image, (center[0]+image.shape[0]//8, image.shape[0]//2), smallSemiCircleSize, 0, 180, 360, blue, cv.FILLED)

cv.imshow(title, image)
cv.waitKey(0)
cv.destroyAllWindows()