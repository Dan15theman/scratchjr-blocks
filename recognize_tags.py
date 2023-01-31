import cv2
from cv2 import cv2
import numpy as np
import os
import imutils

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters_create()

arucoParams.adaptiveThreshWinSizeStep = 5


offset = 25
adim = 250
bdim = 1000


block_dict = {0: 'move left', 1: 'move right', 
2: 'move up', 3: 'move down', 4: 'turn right', 
5: 'turn left', 6: 'hop', 7: 'go home', 8: 'start on message',
9: 'start on green flag', 10: 'start on tap', 
11: 'send message', 12: 'start on bump', 
13: 'pop', 14: 'play sound', 15: 'say', 16: 'grow',
17: 'shrink', 18: 'reset size', 19: 'hide',
20: 'show', 21: 'wait', 22: 'stop', 
23: 'set speed still' , 24: 'set speed mid',
25: 'set speed run', 26: 'repeat', 
27: 'repeat forever', 28: 'go to page',
29: 'end'}


img = cv2.imread(os.path.expanduser('~/Downloads/IMG-9235.jpg'))
# img = imutils.resize(img, width=2000)
# cv2.imshow('img',img)
# cv2.waitKey(0)

print(img.shape)

height = img.shape[0]

(corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

cv2.imshow("Image", img)
cv2.waitKey(0)

if len(corners) > 0:
    ids = ids.flatten()
    # loop over the aruco corners
    for (markerCorner, markerID) in zip(corners, ids):
        # extract the marker corners (which are always returned in
        # top-left, top-right, bottom-right, and bottom-left order)
        lcorners = markerCorner.reshape((4, 2))
        (topLeft, topRight, bottomRight, bottomLeft) = lcorners
        # convert each of the (x, y)-coordinate pairs to integers
        topRight = (int(topRight[0]), int(topRight[1]))
        bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
        bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
        topLeft = (int(topLeft[0]), int(topLeft[1]))

        # draw the bounding box of the ArUCo detection
        cv2.line(img, topLeft, topRight, (255, 0, 0), 10)
        cv2.line(img, topRight, bottomRight, (255, 0, 0), 10)
        cv2.line(img, bottomRight, bottomLeft, (255, 0, 0), 10)
        cv2.line(img, bottomLeft, topLeft, (255, 0, 0), 10)

        # draw the bounding box of the block

        topLeftAdjust = (topLeft[0], height - topLeft[1])
        topRightAdjust = (topRight[0], height - topRight[1])
        bottomLeftAdjust = (bottomLeft[0], height - bottomLeft[1])
        bottomRightAdjust = (bottomRight[0], height - bottomRight[1])

        bottomLeftBlockAdjust = (topRightAdjust[0] + ((adim+offset)/adim)*(bottomLeftAdjust[0]-topRightAdjust[0]),
        topRightAdjust[1] + ((adim+offset)/adim)*(bottomLeftAdjust[1]-topRightAdjust[1]))

        bottomRightBlockAdjust = (bottomLeftBlockAdjust[0] + (bdim/adim)*(bottomRightAdjust[0]-bottomLeftAdjust[0]),
        bottomLeftBlockAdjust[1] + (bdim/adim)*(bottomRightAdjust[1]-bottomLeftAdjust[1]))

        topLeftBlockAdjust = (bottomLeftBlockAdjust[0] + bottomLeftBlockAdjust[1] - bottomRightBlockAdjust[1],
        bottomLeftBlockAdjust[1] - bottomLeftBlockAdjust[0] + bottomRightBlockAdjust[0])

        topRightBlockAdjust = (bottomRightBlockAdjust[0] - bottomLeftBlockAdjust[0] + topLeftBlockAdjust[0],
        bottomRightBlockAdjust[1]+topLeftBlockAdjust[1]-bottomLeftBlockAdjust[1])

        bottomLeftBlock = (int(bottomLeftBlockAdjust[0]), int(height - bottomLeftBlockAdjust[1]))
        bottomRightBlock = (int(bottomRightBlockAdjust[0]), int(height - bottomRightBlockAdjust[1]))
        topLeftBlock = (int(topLeftBlockAdjust[0]), int(height - topLeftBlockAdjust[1]))
        topRightBlock = (int(topRightBlockAdjust[0]), int(height - topRightBlockAdjust[1]))

        cv2.line(img, topLeftBlock, topRightBlock, (0, 255, 0), 10)
        cv2.line(img, topRightBlock, bottomRightBlock, (0, 255, 0), 10)
        cv2.line(img, bottomRightBlock, bottomLeftBlock, (0, 255, 0), 10)
        cv2.line(img, bottomLeftBlock, topLeftBlock, (0, 255, 0), 10)

        # compute and draw the center (x, y)-coordinates of the ArUco
        # marker
        cX = int((topLeft[0] + bottomRight[0]) / 2.0)
        cY = int((topLeft[1] + bottomRight[1]) / 2.0)
        cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)

        # print(str((cX,cY)))

        # draw the ArUco marker ID on the image
        # cv2.putText(img, str(block_dict[markerID]),
        #     (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
        #     0.5, (255, 255, 255), 3)
        
        cv2.putText(img, str(block_dict[markerID]),
            (bottomLeft[0], bottomLeft[1] + 80), cv2.FONT_HERSHEY_SIMPLEX,
            3, (124, 252, 0), 10)
        # show the output image
        cv2.imshow("Image", img)
        cv2.waitKey(0)


ids = ids.flatten()
lower_left = [a[0][0] for a in corners]
new_list = sorted(zip(lower_left, ids), key = lambda x: x[0][0], reverse=False)
newer_list = [block_dict[a[1]] for a in new_list]
print(newer_list)
