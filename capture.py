#!/usr/bin/python3

import cv2

#For captured saved video
cap=cv2.VideoCapture('/home/raksssh/Desktop/adhoc/ml/computer_vision/video_project/Katy_Perry.mp4')


while cap.isOpened():

	status,frame=cap.read()
	cv2.imshow('nn',frame)
	if cv2.waitKey(1) & 0xFF==ord('s'):
                cv2.imwrite('pic.jpg',frame)

	if cv2.waitKey(1) & 0xFF==ord('c'):
		break

#for close all windows
cv2.destroyAllWindows()

#Releasing captured camera frame
cap.release()
