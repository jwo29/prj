# http://blog.comart.io/posts/opencv-rgb-1 참고

import numpy as np, cv2 as cv

logo = cv.imread("images/logo.jpg", cv.IMREAD_COLOR) # 로고 영상 읽기
if logo is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv.split(logo) # 채널 분리, 컬러 영상 -> 3채널 분리

empty = np.zeros(logo.shape, np.uint8) # 빈 채널 생성
blue_img = cv.merge(blue, empty, empty) # 블루 채널 합성
green_img = cv.merge(empty, green, empty) # 그린 채널 합성
red_img = cv.merge(empty, empty, red) # 레드 채널 합성

cv.imshow("logo", logo)
cv.imshow("blue_img", blue_img)
cv.imshow("green_img", green_img)
cv.imshow("red_img", red_img)
cv.waitKey()