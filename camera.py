#!/usr/bin/python3

import cv2
cam=cv2.VideoCapture(0)

while cam.isOpened() :
	status,frame=cam.read()
	img=cv2.flip(frame,1)
	cv2.imshow('new',img)
	
	if  cv2.waitKey(1) & 0xFF == ord('c') :
		break
cv2.destroyAllWindows()
cam.release()
