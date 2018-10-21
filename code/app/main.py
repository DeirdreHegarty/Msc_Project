# TO RUN: FLASK_APP=main.py FLASK_DEBUG=1 flask run

from flask import Flask, request, render_template, session, url_for, redirect, flash
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os, argparse, sys
from flask import send_from_directory
from flask_cors import CORS

sys.path.append("/Users/deirdre/git/Msc_Project/code/app/object_detection")
from object_detection import object_detection_main

app = Flask(__name__)
app.debug = True
CORS(app) # needed for cross-domain requests, allow everything by default

dropzone = Dropzone(app)
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*,video/*'
app.config['DROPZONE_INVALID_FILE_TYPE']
app.config['DROPZONE_REDIRECT_VIEW'] = 'results' 		# redirect to results.html
app.config['DROPZONE_MAX_FILE_SIZE'] = 10

app.config['SECRET_KEY'] = 'secretkey'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)	# name of upload set, allowed extensions
configure_uploads(app, photos) 			# load the configuration for the upload sets

@app.route("/", methods=['GET', 'POST'])
def upload():
	# empty contents of uploads folder
	object_detection_main.delete_uploads()

	# set session for image results
	if "file_urls" not in session:
		session['file_urls'] = []
	
	# uploaded image urls
	file_urls = session['file_urls']

	# clear any unsubmitted images from previous attempts
	session.pop('file_urls', None)

	# image upload from Dropzone
	if request.method == 'POST':
		file_obj = request.files
			
		for f in file_obj:

			file = request.files.get(f)
			app.logger.debug(file.filename)
			
			# save the file & append image urls
			filename = photos.save(file, name=file.filename)
			file_urls.append(photos.url(filename))

		session['file_urls'] = file_urls	
		
	return render_template('upload.html', title='upload')


@app.route('/results')
def results():
	# redirect to home if no images to display
	if "file_urls" not in session or session['file_urls'] == []:
		return redirect(url_for('upload'))

	object_detection_main.load_frozen_model()
	object_detection_main.detect_image()
	
	# set the file_urls and remove the session variable
	file_urls = session['file_urls']
	session.pop('file_urls', None)

	return render_template('results.html',file_urls=file_urls)

