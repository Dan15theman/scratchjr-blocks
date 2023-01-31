import cv2
from cv2 import cv2
import numpy as np

adim = 250

tag = np.zeros((adim, adim, 1), dtype="uint8")
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
# cv2.aruco.drawMarker(arucoDict, 49, 300, tag, 1)

# cv2.imshow('aruco', tag)
# cv2.waitKey(0)

for i in range(50):
    tag = np.zeros((adim, adim, 1), dtype="uint8")
    cv2.aruco.drawMarker(arucoDict, i, adim, tag, 1)
    cv2.imwrite('aruco_tags/' + str(i) + '.png',tag)

