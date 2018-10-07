import numpy as np
import cv2, argparse
from matplotlib import pyplot as plt

def video_feed():
	cap = cv2.VideoCapture(0)

	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

def image_input(img_passed):
	img = cv2.imread(img_passed,cv2.IMREAD_GRAYSCALE)
	cv2.imshow('image', cv2.resize(img,(640,480)))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Object Detection")
	input_group = parser.add_mutually_exclusive_group()
	input_group.add_argument('-v', '--video',
						help="webcam feed input",
						action='store_true')
	input_group.add_argument('-i', '--image',
						help="image input")
	
	args = parser.parse_args()
	if args.video:
		video_feed()
	if args.image:
		image_input(args.image)

	# destroy windows
	cv2.destroyAllWindows()