# The following code is used to watch a video stream, detect Aruco markers, and use
# a set of markers to determine the posture of the camera in relation to the plane
# of markers.
#
# Assumes that all markers are on the same plane, for example on the same piece of paper
#
# Requires camera calibration (see the rest of the project for example calibration)

import numpy
import cv2
import cv2.aruco as aruco


# Constant parameters used in Aruco methods
ARUCO_PARAMETERS = aruco.DetectorParameters_create()
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)

# Create grid board object we're using in our stream
board = aruco.GridBoard_create(
        markersX=2,
        markersY=2,
        markerLength=0.09,
        markerSeparation=0.01,
        dictionary=ARUCO_DICT)

# Create vectors we'll be using for rotations and translations for postures
rvecs, tvecs = None, None

#cam = cv2.VideoCapture('20191016_141102.mp4')
#cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('20191017_100011.mp4')

pos = []

while(cam.isOpened()):
    # Capturing each frame of our video stream
    ret, QueryImg = cam.read()
    if ret == True:
        # grayscale image
        gray = cv2.cvtColor(QueryImg, cv2.COLOR_BGR2GRAY)
    
        # Detect Aruco markers
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
        
        # Make sure markers were detected before printing them out
        if ids is not None :
            # Print corners and ids to the console
            for i, corner in zip(ids, corners):
                print('ID: {}; Corners: {}'.format(i, corner))

            # Outline all of the markers detected in our image
            QueryImg = aruco.drawDetectedMarkers(QueryImg, corners, borderColor=(0, 0, 255))
            
            # Wait on this frame
            ##if cv2.waitKey(0) & 0xFF == ord('q'):
            ##    break
        # add path
        if (ids is not None):
            for i,idd in enumerate(ids):
                print(idd[0])
                if idd[0] == 1:
                    start=(corners[i][0,0,0],corners[i][0,0,1])
                    end=(corners[i][0,1,0],corners[i][0,1,1])
                    #QueryImg = cv2.line(QueryImg,start,end,(255,255,0))
                    ccc=corners[i][0] # shortening
                    centroid_marker = tuple((ccc[0]+ccc[1]+ccc[2]+ccc[3])/4)
                    pos.append(centroid_marker)
                     

        for idx, endelement in enumerate(pos):
            if (idx > 0):
                QueryImg = cv2.line(QueryImg,pos[idx-1],endelement,(255,255,0))
        
        # connect last to first for the mower
       # if (len(pos)>1):
       #     QueryImg = cv2.line(QueryImg,pos[-1],pos[0],(255,255,0))
        
        # Display our image
        cv2.imshow('QueryImage', QueryImg)

    # Exit at the end of the video on the 'q' keypress
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
