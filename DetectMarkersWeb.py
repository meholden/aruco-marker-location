# The following code is used to watch a video stream, detect Aruco markers

# do multiprocessor according to: https://www.geeksforgeeks.org/synchronization-pooling-processes-python/

import numpy
import cv2
import cv2.aruco as aruco
from flask import Flask

## set up web server
app = Flask(__name__)

@app.route("/")
def hello():
    corners,ids = process_cam(0) #"20191017_100011.mp4")
    #print (corners,ids)
    return str(ids)[1:-1]

def process_cam(camname):
    camg = cv2.VideoCapture(camname)
    ret, QueryImg = camg.read()
    #
    #QueryImg = cv2.imread("testimage.png")

    #cv2.imshow('QueryImage', QueryImg)
    if ret == True:
    
        corners, ids = do_arucostuff(QueryImg)
    

    print (corners,ids)
    return corners,ids

## aruco stuff
def do_arucostuff(QueryImg):
    # Capturing each frame of our video stream
        # grayscale image
        gray = cv2.cvtColor(QueryImg, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('tester', gray)
        #cv2.waitKey(1000)
        
        print(ARUCO_DICT)
        # Detect Aruco markers
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
        print(ids)
        return corners,ids

# Constant parameters used in Aruco methods
ARUCO_PARAMETERS = aruco.DetectorParameters_create()
#ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_6X6_250)

#print('reading file')
##qim = cv2.imread("testimage.png")
#cammmm=cv2.VideoCapture('20191017_100011.mp4')
#ret, qim = cammmm.read()
#cv2.imshow('tester', qim)
#cv2.waitKey(100)
#corners,ids = do_arucostuff(qim)
#print (corners,ids)
#cv2.destroyAllWindows()
#
#cam = cv2.VideoCapture('20191016_141102.mp4')
#cam = cv2.VideoCapture(0)
#cam = cv2.VideoCapture('20191017_100011.mp4')

#pos = []

#while(0): #(cam.isOpened()):
#    
#    ret, QueryImg = cam.read()
#    if ret == True:
#    
#        corners, ids = do_arucostuff(QueryImg)
#            
#            
#        # Make sure markers were detected before printing them out
#        if ids is not None :
#            # Print corners and ids to the console
#            for i, corner in zip(ids, corners):
#                print('ID: {}; Corners: {}'.format(i, corner))
#
#            # Outline all of the markers detected in our image
#            QueryImg = aruco.drawDetectedMarkers(QueryImg, corners, borderColor=(0, 0, 255))
#            
#            # Wait on this frame
#            ##if cv2.waitKey(0) & 0xFF == ord('q'):
#            ##    break
#            
#        # find all centroids; add centroid of correct point to path
#        if (ids is not None):
#            for i,idd in enumerate(ids):
#                print(idd[0])
#                start=(corners[i][0,0,0],corners[i][0,0,1])
#                end=(corners[i][0,1,0],corners[i][0,1,1])
#                #QueryImg = cv2.line(QueryImg,start,end,(255,255,0))
#                ccc=corners[i][0] # shortening
#                centroid_marker = tuple((ccc[0]+ccc[1]+ccc[2]+ccc[3])/4)
#                
#                # add correct centroid to path
#                if idd[0] == 1:
#                    pos.append(centroid_marker)
#                         
#        # draw line of centroids
#        for idx, endelement in enumerate(pos):
#            if (idx > 0):
#                QueryImg = cv2.line(QueryImg,pos[idx-1],endelement,(255,255,0))
#        
#        # connect last to first for the mower
#        # if (len(pos)>1):
#        #     QueryImg = cv2.line(QueryImg,pos[-1],pos[0],(255,255,0))
#            
#        # Display our image
#        cv2.imshow('QueryImage', QueryImg)
#
#    # Exit at the end of the video on the 'q' keypress
#    if cv2.waitKey(10) & 0xFF == ord('q'):
#        break
#
#cv2.destroyAllWindows()

# start flask webserver
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


