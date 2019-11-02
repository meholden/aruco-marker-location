import multiprocessing
import cherrypy
import cv2
import cv2.aruco as aruco


def visionproc(cornerset,loc):
    # Constant parameters used in Aruco methods
    ARUCO_PARAMETERS = aruco.DetectorParameters_create()
    #ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)
    ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_6X6_250)

    camg = cv2.VideoCapture(0)
    print('hi')

    while(camg.isOpened()):
        ret, QueryImg = camg.read()
        cv2.imshow('QueryImage', QueryImg)
        if ret == True:
            corn, ids = do_arucostuff(QueryImg,ARUCO_DICT,ARUCO_PARAMETERS)
        
            print(ids)
            # Outline all of the markers detected in our image
            QueryImg = aruco.drawDetectedMarkers(QueryImg, corn, borderColor=(0, 0, 255))
            cv2.imshow('QueryImage', QueryImg)
            # Wait on this frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
#            for i, corner in zip(ids, corn):
#                print('ID: {}; Corners: {}'.format(i, corner))
            loc.acquire()
            if (ids is not None):
                for i,idd in enumerate(ids):
                    cornerset[i]=idd
            loc.release()
            
    cv2.destroyAllWindows()


## aruco stuff
def do_arucostuff(QueryImg,ARUCO_DICT,ARUCO_PARAMETERS):
    # Capturing each frame of our video stream
    # grayscale image
    gray = cv2.cvtColor(QueryImg, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('tester', gray)
    #cv2.waitKey(1000)
    
    # Detect Aruco markers
    corn, ids, rejectedImgPoints = aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
    return corn,ids



class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        lock.acquire()
        ssstr = "corners: {}".format(corners[0:-1])
        lock.release()
        return ssstr
    
if __name__ == "__main__":
    corners = multiprocessing.Array('i',9*30)
    
    lock = multiprocessing.Lock()
    
    p1 = multiprocessing.Process(target=visionproc, args=(corners,lock))
    print("starting")
    p1.start()
    print("started")
#    visionproc(corners,lock)

    cherrypy.quickstart(HelloWorld())
    
    p1.join()
    #p2.join()
        