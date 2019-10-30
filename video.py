import cv2

def gray(image):
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)#cvtColor converts an image from one color space to another
    return gray

cap = cv2.VideoCapture("G:\\opencv\\25 Best Moments from F.R.I.E.N.D.S - Netflix.mp4")
while(cap.isOpened()):
	_,frame = cap.read()
	gray_image = gray(frame)
	cv2.imshow('result',gray_image)
	cv2.waitKey(1)
