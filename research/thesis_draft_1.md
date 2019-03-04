# Thesis draft 1 

## Abstract

The intention of this project is to explore the encoding of meaning into audio, and how that in turn represents its visual counterpart. Using a machine learning framework and audio references, photographs will be dissected into their object content labels. These labels will describe what is present in each image. Once images have been analysed, an audio sample that best describes each object label will be retrieved from an audio reference list. The sound descriptions are then recreated in a binaural sound simulation of the input image. Multiple detected objects add to the richness and immersion of the scene. The result is to create an auditory explanation of the scene through sounds instead of words; to experience a description of an image void of language.


## Motivation

Much research has been invested in the dissection of images into text and speech; both channels embedded in human interpretation and understanding. Text-based descriptions are heavily restricted by language. Meaning can become lost between the translation of one language description to another. Each layer of abstraction introduces an opportunity for miscommunication or ill interpretation of the visual. Budd speaks about the lexical ambiguity of language-based descriptions, explaining how "a “mole” may be a burrowing animal or an information gatherer in an organization"[@budd]. This ambiguity not only means that a description may be interpreted in different ways in a given language, but also means that once translated into another language, the chosen interpretation may have been inaccurate. This new inaccurate description may then be subjected to its own language specific misinterpretations. Thus, creating a tree of correct and incorrect possible descriptions of an event.

"A picture is worth a thousand words", an English idiom, encapsulates the idea that there are limits associated with language-based descriptions of a scene. Ultimately, there can only ever be a finite amount of words that will accurately describe the seen. This idiom is said to be derived from an advertisement in Syracuse Post Standard newspaper - "Use a picture. It's worth a thousand words."[@englishidiom].

Listening to speech describing a narrative can reveal to the listener, factual data about the scene. Because the predominant exploration of image has been in relation to its conversion into a language-based media, user experience and immersion have been set to the background. 

The visual and auditory systems overlap; each sensory system providing the missing piece for the other [@seeingsounds]. Synaesthesia describes the impression of one sense on another, whereas cognition can reflect a learned association of the same. Audio has a huge affect on the experience of an event because the "auditory system gives more precise temporal information and appears to dominate perception of when events occur" [@seeingsounds2]. It is over time that we learn how duration and auditory cognition encodes importance of event.

An auditory response that is produced naturally by an object can be a pure description of event. It evokes a more primitive response that reduces the misinterpretation of its visual counterpart. It is free of language and is an uninhibited description of a real-time interaction. Auditory response is less likely to become tarnished by misinterpretation, because it is not dependant on language or speech. What is meant by this is, more can be attributed to hearing the sound an object produces as opposed to being presented with a sentence that describes the same. This project seeks to evoke a hearing of "another story behind the main narrative, the hidden story arising from the seat of the unconscious"[@soundandsilence]. A sense of otherness is created through the use of audio samples as opposed to a formal description of the scene through sentences, synthesised by a vocoder. 

## Problem Statement

The visual and auditory systems overlap; each sensory system providing the missing piece for the other [@seeingsounds]. Synaesthesia describes the impression of one sense on another, whereas cognition can reflect a learned association of the same. Audio has a huge affect on the experience of an event because the "auditory system gives more precise temporal information and appears to dominate perception of when events occur" [@seeingsounds2]. It is over time that we learn how duration and auditory cognition encodes importance of event.

According to 2016 Census, the percentage of people with visual impairment increased by 6% between 2011 - 2016. This means that in 2016, 54,810 people living in Ireland were acknowledged as being visually impaired[@censusprofile9]. The work of Jiang, Lin and Qu addresses real-time image to speech processing. Their work outlines the implementation of a system where "both visual object and audio sound can be spatially localized"[@letblindsee]. Although this project implements spatial sound techniques for placement of audio in space, the use of description through language removes the participant from the immediate experience of the scene.

The NCSE Press Release outlines that 1 in every 65 children in Ireland are diagnosed as being on the Autistic spectrum[@ncsepress]; this equates to 1.5% of students attending school in 2016. This demographic could be considered to be an audience that would benefit greatly from a tool that provides interactive visual and aural support for learning about objects in context. Creating an alternative to textbook based learning allows for a more bespoke learning experience. In their paper, Tanner, Dixon and Verenikina state that "visual learning dimension incorporated in digital technologies is supportive of the visual modality of students with ASD"[@autismdigi].


---

## Topic Material

Although there exists multiple tools for the conversion if image into another format, none implement image to sound in the same way as is intended by this project.  

VizWiz[@vizwiz] and TapTapSee[@taptap] are examples of two mobile applications designed to assist the visually impaired. VizWiz implements "quikTurkit", a project specific feature built using the TurKit API[@turkit] for recruiting human workers to executing tasks on Mechanical Turk[@mechanicalturk]. The application makes use of image, voice recording and speech to text, to allow users to receive information about a specific object or scene. Its academic paper highlights issues regarding speech to text conversion, stating that it has a 15.8% success rate in accurately converting voice recorded questions into text for later answering. Although image classification and analysis relies on this conversion, the human classifier can listen to the voice recorded question captured by the user. Therein lies a possible issue or restriction caused by language based analysis. 

Both VizWiz and TapTapSee use VoiceOver[@voiceover], a gesture-based screen reader on iOS. However, TapTapSee does all image classifications automatically as opposed to outsourcing to Mechical Turk's human workers. Because of the nature of the application, it cannot answer the same multitude of questions as VizWiz; it can simply classify objects in a given image and speak the answer to the user along with displaying the text. Although the application allows for multiple languages, it does not supply the user with information such as position, thus removing the user from the immediate experience of object interaction.

Gupta and Mannem's work explores the synthesis of anthropomorphic descriptions through the use of image annotations in the form of captioning. Their work puts emphasis on how "human-like descriptions can be generated" through task-based evaluation of results, and the need for "automatic conversion of image annotations to natural language"[@annotationdesc]. Because their predominant focus is on human-like descriptions of images, the importance of description has been places on factual labelling of images as opposed to the direct experience of image through non-language based channels.

Perhaps the closest relating research to the work outlined in this paper, is outlined in 'The Visual Microphone: Passive Recovery of Sound from Video'. High speed footage catpures vibrations on the surface of an object. This footage then allows for the sound that has been encoded in the objects surface to be recovered[@visualmic]. The object in question acts as the medium through which sound is visualised. This allows for a more pure retrieval of audio from visual. Although the user can remain present within the description of event, the object that is being analysed is acting as a proxy amplifier for sound events tied to other objects. Therefore the project does not recreate sound tied to a specific object, but the sound of surrounding objects.

Krishnan, Porkodi and Kanimozhi take a purely visual approach to audio conversion. Their work allows for the production of audio directly from an image. Sustain and frequency is determined by the ouput of canny edge detection on an image; low frequencies captured in horizontal edges, and higher frequencies in the vertical edges[@cannyaudio].


## Technical material


---

# The Solution

## Website - User upload image

The main languages used to develop this web application are Javascript and Python, with Flask providing much of the routing and data handling functionalities. Flask is a lightweight framework, written in Python, that allows for the development of web applications [@flask].   

The web interface uses `Flask-Dropzone` [@flask_dz] and `Flask-Uploads` [@flask_up] for file uploading fucntionality. Selected files are validated against a list of predefined accepted file types. The dropzone will reject a file if it is not of an accepted format. Client-side sessions are used for differentiating and managing both original and image detected files. 

Once a user has sucessfully uploaded a file, Flask passes the file to Tensorflow for object detection. After detection has occurred, Flask receives the processed image along with metadata including detected objects' locations in the input image, name and a reference to the detected objects' associated sounds. Flask then renders the retrieved data into HTML. The associated sounds are rendered inside the source of html audio tags, and are later triggered using WebAudio API, an API for audio manipulation written in Javascript[@web_audio].


Once in the results route, audio files relating to the detected classes are retrieved. Each audio file is rendered inside the source of a html audio tag and is then triggered using the javascript API, Web Audio API [@web_audio]. Web Audio API offers PannerNodes [@web_audio_pan], which allow for each audio file to be panned according to their position in the detected input image. BufferLoader [@web_audio_buf] used alongside the PannerNodes simulate the placement of audio on a virtual 3-dimensional audio plane. A more detailed explanation of this functionality can be found in Appendix A under the heading 'Sound Retrieval'.


## image detection of image

Tensorflow can then retrieve the images from /uploads and perform object detection. TensorFlow is an open-source software library for numerical computation, and is well known for its use in the fields of machine learning and deep learning [@tensorflow]. The dataset used by the CNN model is COCO [@coco].

An output image is generated and written to /detected_images; this image (seen in Figure 5) will have bounding boxes drawn around the detected objects, along with labels containing the detected class and percentage of AP (average precision). The list of classes present in each image is passed from the Tensorflow module to Flask, to be rendered as a list in the browser along with the originally uploaded image

## lable retrieval

## sound retrieval, rendering and triggering
