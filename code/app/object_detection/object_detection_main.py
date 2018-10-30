#!/usr/bin/env python
# coding: utf-8

import numpy as np
import six.moves.urllib as urllib
import tensorflow as tf
import matplotlib.image as mpimg
import os, os.path, sys, tarfile, zipfile, cv2, shutil

from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from pathlib import Path
from os.path import splitext

# path to project 
sys.path.append("/Users/deirdre/git/Msc_Project/code/app/")
from object_detection.utils import ops as utils_ops

if StrictVersion(tf.__version__) < StrictVersion('1.9.0'):
	raise ImportError('Please upgrade your TensorFlow installation to v1.9.* or later!')

# imports from the object detection module.
from utils import label_map_util
from utils import visualization_utils as vis_util
from utils.visualization_utils import *
# *********************** end of imports ******************************* #

# Variables:
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing 
# `PATH_TO_FROZEN_GRAPH` to point to a new .pb file.  
# 
# using "SSD with Mobilenet" model. 
# See [detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) 
# for a list of other models that can be run out-of-the-box with varying speeds and accuracies.

# Model to download
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

def check_if_model_present():
	'''
			check if model is present in directory 
			and download if not present
	'''
	# check if model downloaded & download if not present
	if os.path.exists(MODEL_NAME):
		print('Model already downloaded')
	else:
		print('Downloading model...')
		downloadModel()

def downloadModel():
	'''Download model (specified by variable MODEL_FILE)
	'''
	opener = urllib.request.URLopener()
	opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
	tar_file = tarfile.open(MODEL_FILE)
	for file in tar_file.getmembers():
		file_name = os.path.basename(file.name)
		if 'frozen_inference_graph.pb' in file_name:
			tar_file.extract(file, os.getcwd())

def load_frozen_model():
	'''Load a (frozen) Tensorflow model into memory.
	'''
	global detection_graph 
	global category_index
	detection_graph = tf.Graph()
	with detection_graph.as_default():
		od_graph_def = tf.GraphDef()
		with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
			serialized_graph = fid.read()
			od_graph_def.ParseFromString(serialized_graph)
			tf.import_graph_def(od_graph_def, name='')


	# ## Loading label map (COCO)
	# Label maps map indices to category names
	# returns a dictionary mapping integers to 
	# appropriate string labels
	category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

def run_inference_for_single_image(image, graph):
	with graph.as_default():
		with tf.Session() as sess:
			# Get handles to input and output tensors
			ops = tf.get_default_graph().get_operations()
			all_tensor_names = {output.name for op in ops for output in op.outputs}
			tensor_dict = {}
			for key in [
					'num_detections', 'detection_boxes', 'detection_scores',
					'detection_classes', 'detection_masks'
			]:
				tensor_name = key + ':0'
				if tensor_name in all_tensor_names:
					tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
							tensor_name)
			if 'detection_masks' in tensor_dict:
				# The following processing is only for single image
				detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
				detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
				# Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
				real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
				detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
				detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
				detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
						detection_masks, detection_boxes, image.shape[0], image.shape[1])
				detection_masks_reframed = tf.cast(
						tf.greater(detection_masks_reframed, 0.5), tf.uint8)
				# Follow the convention by adding back the batch dimension
				tensor_dict['detection_masks'] = tf.expand_dims(
						detection_masks_reframed, 0)
			image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

			# Run inference
			output_dict = sess.run(tensor_dict,
														 feed_dict={image_tensor: np.expand_dims(image, 0)})

			# all outputs are float32 numpy arrays, so convert types as appropriate
			output_dict['num_detections'] = int(output_dict['num_detections'][0])
			output_dict['detection_classes'] = output_dict[
					'detection_classes'][0].astype(np.uint8)
			output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
			output_dict['detection_scores'] = output_dict['detection_scores'][0]
			if 'detection_masks' in output_dict:
				output_dict['detection_masks'] = output_dict['detection_masks'][0]
	return output_dict

def load_image_into_numpy_array(image):
	(im_width, im_height) = image.size
	return np.array(image.getdata()).reshape(
			(im_height, im_width, 3)).astype(np.uint8)

def delete_uploads():
	shutil.rmtree('/Users/deirdre/git/Msc_Project/code/app/uploads')
	os.mkdir('/Users/deirdre/git/Msc_Project/code/app/uploads')

def detect_image():
	PATH_TO_TEST_IMAGES_DIR = '/Users/deirdre/git/Msc_Project/code/app/uploads'

	ACCEPTED_FILE_TYPES = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
	TEST_IMAGE_PATHS = [file for file in os.listdir(PATH_TO_TEST_IMAGES_DIR) if Path(file).suffixes[0] in ACCEPTED_FILE_TYPES]
	DETECTED_IMAGES = '/Users/deirdre/git/Msc_Project/code/app/detected_images'

	# Size, in inches, of the output images.
	IMAGE_SIZE = (12, 8)
	# import pdb; pdb.set_trace()

	for image_path in TEST_IMAGE_PATHS:
		image = Image.open(os.path.join(PATH_TO_TEST_IMAGES_DIR,image_path))

		# the array based representation of the image will be used later in order to prepare the
		# result image with boxes and labels on it.
		image_np = load_image_into_numpy_array(image)
		# Expand dimensions since the model expects images to have shape: [1, None, None, 3]
		image_np_expanded = np.expand_dims(image_np, axis=0)

		# Actual detection.
		output_dict = run_inference_for_single_image(image_np, detection_graph)

		# Visualization of the results of a detection.
		vis_util.visualize_boxes_and_labels_on_image_array(
				image_np,
				output_dict['detection_boxes'],
				output_dict['detection_classes'],
				output_dict['detection_scores'],
				category_index,
				instance_masks=output_dict.get('detection_masks'),
				use_normalized_coordinates=True,
				line_thickness=8)

		# currently have issue with saving output issue
		# plt.figure(figsize=IMAGE_SIZE)
		# plt.imsave(image_path, image_np)



def detect_webcam():
	while True:
	  ret, image_np = cap.read() # returns as a numpy array so dont need to convert

	  # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
	  image_np_expanded = np.expand_dims(image_np, axis=0)

	  # Actual detection.
	  output_dict = run_inference_for_single_image(image_np, detection_graph)

	  # Visualization of the results of a detection.
	  vis_util.visualize_boxes_and_labels_on_image_array(
		  image_np,
		  output_dict['detection_boxes'],
		  output_dict['detection_classes'],
		  output_dict['detection_scores'],
		  category_index,
		  instance_masks=output_dict.get('detection_masks'),
		  use_normalized_coordinates=True,
		  line_thickness=8)

	  cv2.imshow('prototype', cv2.resize(image_np, (800,600)))
	  if cv2.waitKey(25) & 0xFF == ord('q'):
		  cv.destroyAllWindows()
		  break 

# check, load then detect
# check_if_model_present()
# load_frozen_model()
# detect_image()
