

import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)


# make a grid of markers
#fig = plt.figure()
#nx = 4
#ny = 3
#for i in range(1, nx*ny+1):
#    ax = fig.add_subplot(ny,nx, i)
#    img = aruco.drawMarker(aruco_dict,i, 700)
#    plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
#    ax.axis("off")
#
#plt.show()

# save a single marker to pdf file
fig2=plt.figure()
imrkr = 1 # which marker to print
pixmarker = 800
img = aruco.drawMarker(aruco_dict,imrkr, pixmarker)
plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
plt.axis("off")
filemarker = "marker" + str(imrkr) + ".pdf"
print(filemarker)
plt.savefig(filemarker)    
plt.show()

