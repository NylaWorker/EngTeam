import cv2 
import numpy

cam = cv2.VideoCapture(0)

while(True):
	ret, frame = cam.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow("frame",gray)
	if cvw.waitKey(1) & 0xFF== ord("q"):
		break
cam.realese()
cv2.destroyAllWindows()
