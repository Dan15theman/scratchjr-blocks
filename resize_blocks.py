import cv2
from cv2 import cv2
import numpy as np
import os

for i in range(1,41):
    old_block = cv2.imread(os.path.expanduser('~/Desktop/block_screenshots/' + str(i) + '.png'))
    resized_block = cv2.resize(old_block, (1000,1000))
    cv2.imwrite('blocks/block' + str(i-1) + '.png', resized_block)

