import cv2
from cv2 import cv2
import numpy as np
import os

adim=250
bdim=1000
offset = 25

for i in range(40):
    block = cv2.imread('blocks/block' + str(i) + '.png')
    mark = cv2.imread('aruco_tags/' + str(i) + '.png')
    block[bdim-adim-offset:bdim-offset, offset:adim+offset] = mark
    cv2.imwrite('tagged_blocks/' + str(i) + '.png', block)



