import cv2 as cv 
import numpy as np 

camera = cv.VideoCapture("video.mp4")
fourcc = cv.VideoWriter_fourcc(*'mp4v')
output_video = cv.VideoWriter('canny_video.mp4', fourcc, 23.976, (1280,720), isColor=False)

while camera.isOpened():

	ret, frame = camera.read()
	if ret:
		edges = cv.Canny(frame, 50, 50)
		edges = cv.resize(edges, (1280,720))
		output_video.write(edges)
		cv.imshow('frame', edges)
		c = cv.waitKey(1)
		if c & 0xFF == ord('q'):
			break
	else:
		break 

camera.release()
output_video.release()


"""camera = cv.VideoCapture(0)
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
cv.destroyAllWindows()"""