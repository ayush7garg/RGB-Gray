import cv2

def gray(image):
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)#cvtColor converts an image from one color space to another
    return gray

cap = cv2.VideoCapture("path of the video file")
while(cap.isOpened()):
	_,frame = cap.read()
	gray_image = gray(frame)
	cv2.imshow('result',gray_image)
	cv2.waitKey(1)
