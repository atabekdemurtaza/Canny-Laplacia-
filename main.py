import cv2 as cv 
import numpy as np 

camera = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out    = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
	_, frame = camera.read()

	cv.imshow('Camera', frame)

	laplacian = cv.Laplacian(frame, cv.CV_64F) #бит
	laplacian = np.uint8(laplacian)
	cv.imshow('Laplacian', laplacian)

	edges = cv.Canny(frame, 100, 100)
	cv.imshow('Canny', edges)

	if cv.waitKey(5) == ord('x'):
		break 

camera.release()
out.release()
cv.destroyAllWindows()