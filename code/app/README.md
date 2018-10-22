## Image Labelleing Prototype [Weeks 1 - 5]

### TO RUN: 

```python
FLASK_APP=main.py FLASK_DEBUG=1 flask run
```

### File Structure

```
app
├── detected_images
│   ├── dog.jpg
│   └── dog_car.jpeg
│
├── main.py
│
├── object_detection
│   ├── __init__.py
│   │
│   ├── data
│   │   ├── __init__.py
│   │   └── mscoco_label_map.pbtxt
│   │
│   ├── object_detection_main.py
│   │
│   ├── ssd_mobilenet_v1_coco_2017_11_17.tar.gz
│   │
│   ├── test_images
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── image_info.txt
│   └── utils
│       ├── __init__.py
│       ├── label_map_util.py
│       ├── label_map_util_test.py
│       ├── visualization_utils.py
│       └── visualization_utils_test.py
│
├── ssd_mobilenet_v1_coco_2017_11_17
│   └── frozen_inference_graph.pb
│
├── templates
│   ├── results.html
│   ├── skeleton.html
│   └── upload.html
│
└── uploads
    ├── dog.jpg
    └── dog_car.jpeg

```

*Image Labelling Prototype* is a Flask application with a TensorFlow backend. The prototype offers the following functionality:

* To upload images:
  * drag and drop image functionality
  * file explorer to choose upload image
  * **accepted image extensions = '.jpg', '.jpeg', 'png'**
* Output object detected image with bounding boxes & labels
* Output a list of detected classes (defined by COCO dataset)   

When an image is uploaded to the application, Flask passes the image to the `/uploads`. Tensorflow can then retrieve the images from `/uploads` and perform object detection.   

An output image is generated and written to `/detected_images`; this image will have bounding boxes drawn around the detected objects, along with labels containing the detected class and percentage of AP (average precision). The list of classes present in each image is passed from the Tensorflow module to Flask, to be created in the DOM and displayed in the browser.  

### object_detection_main.py (TensorFlow)
* check if model is downloaded, and download if not present
* load frozen TensorFlow 
* load the label map [imported from `label_map_util.py`]
* delete previously uploaded images
* loop through images in `/uploads`
* load image into numpy array & reshape for tf model 
* feed images to tf model 
* detect objects & calculate AP
* visualise the result [imported from `visualization_utils.py`]

*There is functionality present for live camera feed, however, I do not currently have a GPU (works with CPU but very slow and jumpy).*

### main.py (Flask)
* `@app.route('/results')`
  * uses `flask_dropzone` and `flask_uploads` to allow for drag and drop functionality for image uploads
  * set allowed upload types
  * sends accepted images to `/uploads`
  * checks contents of `/uploads` and redirects to `/results`
* `@app.route('/results')`
  * triggers tf model to load
  * triggers tf object detection on uploaded images
  * accepts list of detected classes & displays list along with uploaded image
