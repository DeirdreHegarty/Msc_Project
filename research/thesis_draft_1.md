---
title:              Thesis Draft
author:             Deirdre Hegarty, 15187799
email:              deirdre.hegarty@mu.ie
date:               March, 2019
supervisor: 		Dr. Charles Markham
department: 		Department of Computer Science

toc:                yes
fontsize:           11pt
geometry:           margin=25mm
linespacing:        1.15
papersize:          A4
link-citations:     true
...
\pagebreak

# Thesis draft 1 

## Abstract

The intention of this project is to explore the encoding of meaning into audio, and how that in turn represents its visual counterpart. Using a machine learning framework and audio references, photographs will be dissected into their object content labels. These labels will describe what is present in each image. Once images have been analysed, an audio sample that best describes each object label will be retrieved from an audio reference list. The sound descriptions are then recreated in a binaural sound simulation of the input image. Multiple detected objects add to the richness and immersion of the scene. The result is to create an auditory explanation of the scene through sounds instead of words; to experience a description of an image void of language.


## Motivation

Much research has been invested in the dissection of images into text and speech; both channels embedded in human interpretation and understanding. Text-based descriptions are heavily restricted by language. Meaning can become lost between the translation of one language description to another. Each layer of abstraction introduces an opportunity for miscommunication or ill interpretation of the visual. Budd speaks about the lexical ambiguity of language-based descriptions, explaining how "a “mole” may be a burrowing animal or an information gatherer in an organization"[@budd]. This ambiguity not only means that a description may be interpreted in different ways in a given language, but also means that once translated into another language, the chosen interpretation may have been inaccurate. This new inaccurate description may then be subjected to its own language specific misinterpretations. Thus, creating a tree of correct and incorrect possible descriptions of an event.

"A picture is worth a thousand words", an English idiom, encapsulates the idea that there are limits associated with language-based descriptions of a scene. Ultimately, there can only ever be a finite amount of words that will accurately describe the seen. This idiom is said to be derived from an advertisement in Syracuse Post Standard newspaper - "Use a picture. It's worth a thousand words."[@englishidiom].

Listening to speech describing a narrative can reveal to the listener, factual data about the scene. Because the predominant exploration of image has been in relation to its conversion into a language-based media, user experience and immersion have been set to the background. 

The visual and auditory systems overlap; each sensory system providing the missing piece for the other [@seeingsounds]. Synaesthesia describes the impression of one sense on another, whereas cognition can reflect a learned association of the same. Audio has a huge affect on the experience of an event because the "auditory system gives more precise temporal information and appears to dominate perception of when events occur" [@seeingsounds2]. It is over time that we learn how duration and auditory cognition encodes importance of event.

An auditory response that is produced naturally by an object can be a pure description of event. It evokes a more primitive response that reduces the misinterpretation of its visual counterpart. It is free of language and is an uninhibited description of a real-time interaction. Auditory response is less likely to become tarnished by misinterpretation, because it is not dependent on language or speech. What is meant by this is, more can be attributed to hearing the sound an object produces as opposed to being presented with a sentence that describes the same. This project seeks to evoke a hearing of "another story behind the main narrative, the hidden story arising from the seat of the unconscious"[@soundandsilence]. A sense of otherness is created through the use of audio samples as opposed to a formal description of the scene through sentences, synthesised by a vocoder. 

## Problem Statement

According to 2016 Census, the percentage of people with visual impairment increased by 6% between 2011 - 2016. This means that in 2016, 54,810 people living in Ireland were acknowledged as being visually impaired[@censusprofile9]. The work of Jiang, Lin and Qu addresses real-time image to speech processing. Their work outlines the implementation of a system where "both visual object and audio sound can be spatially localized"[@letblindsee]. Although this project implements spatial sound techniques for placement of audio in space, the use of description through language removes the participant from the immediate experience of the scene.

The NCSE Press Release outlines that 1 in every 65 children in Ireland are diagnosed as being on the Autistic spectrum[@ncsepress]; this equates to 1.5% of students attending school in 2016. This demographic could be considered to be an audience that would benefit greatly from a tool that provides interactive visual and aural support for learning about objects in context. Creating an alternative to textbook based learning allows for a more bespoke learning experience. In their paper, Tanner, Dixon and Verenikina state that "visual learning dimension incorporated in digital technologies is supportive of the visual modality of students with ASD"[@autismdigi].


---

## Topic Material

Although there exists multiple tools for the conversion if image into another format, none implement image to sound in the same way as is intended by this project.  

VizWiz[@vizwiz] and TapTapSee[@taptap] are examples of two mobile applications designed to assist the visually impaired. VizWiz implements "quikTurkit", a project specific feature built using the TurKit API[@turkit] for recruiting human workers to executing tasks on Mechanical Turk[@mechanicalturk]. The application makes use of image, voice recording and speech to text, to allow users to receive information about a specific object or scene. Its academic paper highlights issues regarding speech to text conversion, stating that it has a 15.8% success rate in accurately converting voice recorded questions into text for later answering. Although image classification and analysis relies on this conversion, the human classifier can listen to the voice recorded question captured by the user. Therein lies a possible issue or restriction caused by language based analysis. 

Both VizWiz and TapTapSee use VoiceOver[@voiceover], a gesture-based screen reader on iOS. However, TapTapSee does all image classifications automatically as opposed to outsourcing to Mechanical Turk's human workers. Because of the nature of the application, it cannot answer the same multitude of questions as VizWiz; it can simply classify objects in a given image and speak the answer to the user along with displaying the text. Although the application allows for multiple languages, it does not supply the user with information such as position, thus removing the user from the immediate experience of object interaction.

Gupta and Mannem's work explores the synthesis of anthropomorphic descriptions through the use of image annotations in the form of captioning. Their work puts emphasis on how "human-like descriptions can be generated" through task-based evaluation of results, and the need for "automatic conversion of image annotations to natural language"[@annotationdesc]. Because their predominant focus is on human-like descriptions of images, the importance of description has been places on factual labelling of images as opposed to the direct experience of image through non-language based channels.

Perhaps the closest relating research to the work outlined in this paper, is outlined in 'The Visual Microphone: Passive Recovery of Sound from Video'. High speed footage catpures vibrations on the surface of an object. This footage then allows for the sound that has been encoded in the objects surface to be recovered[@visualmic]. The object in question acts as the medium through which sound is visualised. This allows for a more pure retrieval of audio from visual. Although the user can remain present within the description of event, the object that is being analysed is acting as a proxy amplifier for sound events tied to other objects. Therefore the project does not recreate sound tied to a specific object, but the sound of surrounding objects.

Krishnan, Porkodi and Kanimozhi take a purely visual approach to audio conversion. Their work allows for the production of audio directly from an image. Sustain and frequency is determined by the output of canny edge detection on an image; low frequencies captured in horizontal edges, and higher frequencies in the vertical edges[@cannyaudio].

---

# The Solution

## Website

The decision of creating a web-based application stemmed from the intention of providing a readily accessible tool to a large audience. It was thought that there would be a restriction of audience if the application were to be a native application for mobile devices or desktop machines. The main advantage to making the application web-based, is the fact that it can reach a large audience on a wide variety of devices and operating systems. However, currently Apple iOS or Safari is not supported.

The main languages used to develop this web application are JavaScript and Python, with Flask providing much of the routing and data handling functionalities. Flask is a lightweight framework, written in Python, that allows for the development of web applications [@flask].   

The web interface uses `Flask-Dropzone` [@flask_dz] and `Flask-Uploads` [@flask_up] for file uploading functionality. Selected files are validated against a list of predefined accepted file types. The dropzone will reject a file if it is not of an accepted format. Client-side sessions are used for differentiating and managing both original and image detected files. 

Once a user has successfully uploaded a file, Flask passes the file to Tensorflow for object detection. After detection has occurred, Flask receives the processed image along with meta-data including detected objects' locations in the input image, name and a reference to the detected objects' associated sounds. Flask then renders the retrieved data into HTML. The associated sounds are rendered inside the source of HTML audio tags, and are later triggered using WebAudio API, an API for audio manipulation written in JavaScript[@web_audio].

## Object Detection

Object detection is handled by TensorFlow. TensorFlow is an open-source library for numerical computation, and is well known for its use in the fields of machine learning and deep learning [@tensorflow]. The dataset used by the Convolutional Neural Network (CNN) model is Microsoft COCO [@coco]. The Microsoft COCO dataset contains 91 "thing" object categories. Compared to PASCAL VOC 2012[@pascal], SUN[@sun] and ImageNet [@imagenet], Microsoft COCO has more instances per category, and focusses on the detection of objects in their natural contexts. 

The output image generated by Tensorflow contains bounding boxes with labels that display the detected class and percentage of AP (average precision) of each detected object. Extra functionality is added to the Tensorflow source code to facilitate the retrieval of bounding box coordinates, and detected object names as strings. 

The retrieved coordinates contain the min and max X and Y values for each bounding box rendered in the output image. It is important that the coordinates that are retrieved correlate with their associated object, as they are used for the spatial placement of each objects' audio. The list of strings that contain each objects' names are equally as important as they are rendered in browser as a list, and used for associated sound identification and retrieval. 

Originally Keras, a high-level neural networks API [@keras] which can run on top of Tensorflow, was considered to be good tool for this project. Using Keras would have proven problematic later in the project when retrieving audio for corresponding object classes. Keras provides clients the use of simple APIs, in turn limiting the control over data manipulation. Because of the decision to use Tensorflow directly, it was possible to add to and alter the code for the CNN model, creating extra functionality that was not already present.


## Label Retrieval

After the input image has been processed by Tensorflow label retrieval takes place. A series of method calls retrieve the location for each detected objects and their associated sounds from a JSON array. A dictionary mapping sounds to location is then returned to Flask.

Each JSON object contains the name, id, display name and path to associated sound file. The name and id keys contain the same values as are used by the Tensorflow CNN, while the display name key references the name of the detected object as it is to be displayed.

To calculate the binaural audio position, the center point of the object is found. Next a transformation is applied to transform the object centre point, which is relative to the image(0...1), to the range of the audio panner (-1...1). The following equation reflects the afore mentioned transformation.

\begin{align}
& \left( \frac{X_{min} + X_{max}}{2} \right)                             & \text{Find the centre point of the object}                  & \nonumber \\
& \left( \left(\frac{X_{min} + X_{max}}{2}\right) - 0.5 \right)          & \text{Shift the range from (0 \dots 1) to (-0.5 \dots 0.5)} & \nonumber \\
& \left( \left(\frac{X_{min} + X_{max}}{2}\right) - 0.5 \right) \times 2 & \text{Multiply by two to give a range of (-1 \dots 1)}      & \nonumber \\ \nonumber
\end{align}


## Sound Retrieval and Triggering

Before research had taken place, it was assumed that Python would provide a perfect solution for triggering multiple audio files via different channels. An initial solution for dynamically retrieving audio relating to specific object classes was developed using Pygame [@pygame]. However, there came an issue when integrating the Pygame module into the Flask application. Pygame and Flask compete to work on the main thread; throwing errors. Instead of trying to process the audio functionality in the backend, a client-side solution using Web Audio API [@web_audio] was implemented. Written in JavaScript, Web Audio API allows for the same functionality as Pygame, without restricting audio samples to a specific number of channels.

JavaScript is used to map each HTML audio tag to a function that extracts the pan value from the tag's class attribute. The pan value and audio file is loaded into a buffer. Each audio file in the buffer is triggered at 2 second intervals. Web Audio API offers PannerNodes [@web_audio_pan], which allow for each audio file to be panned relative to their position in the detected input image. BufferLoader [@web_audio_buf] used alongside the PannerNodes simulate the placement of audio on a virtual 3-dimensional audio plane. A more detailed explanation of this functionality can be found in Appendix A under the heading 'Sound Retrieval'.

Currently this project does not make use of an API for retrieving audio. FreeSound offers an API for the retrieval of specific and associated sounds[@freesound]. The idea of incorporating an API would make for dynamic sound retrieval for attaching multiple sound profiles to a specific object; however, the poor quality of a large percentage of sounds available via FreeSound API did not validate a decision to include it in the project. An alternate decision was made to store audio files in a local directory. The files are sourced from two royalty free sound effect libraries, Zapsplat[@zapsplat] and AudioHero[@audiohero]. 

The decision of placing a 2 second gap between the triggering of each audio sample was an instinctual and intuitive one. After researching the motive behind this subconscious decision it was uncovered that there appears to be an agreed upon a standard from the 1980s regarding the 2 second default gap between audio tracks on a CD. Although multiple forums contain arguments as to whether the standard was really a standard at all, it is said that "In 1980 Philips and Sony produced their Red Book, which laid down all the standards for compact discs" [@bbc]. In its online manual "Splitting a recording into separate tracks", Audacity reference the 2 second gap advising to "add the standard 2-second gap between each track" while exporting multiple tracks to a CD [@audacity]. 

There was a conscious decision made to retrieve only true sounds emitted by an object, and not relative sounds to where an object resides. Because of this decision, there are many detected objects that do not have an associated sound; the objects in question are silent and do not produce any sounds themselves. With this decision comes an issue regarding context. A plate that is flat on a table makes no noise, however there is an anticipation of sound if presented with an image of a plate falling towards the ground.
This is a bigger question that cannot immediately be addressed  as it is out of the scope of this project.

## Documentation and Version Control

Throughout the duration of the project Git[@git] has been used to track code progression and documentation. Git, along with Github[@github] allows for local and remote versions of the project to exist. While working on a specific feature Git is used to locally store and document code changes. Once a more realised version of the feature is completed, the changes are then pushed to the remote repository on Github. The repository that contains the project code is public and facilitates subscribers to track any changes to the code base, refinement of features, bug fixes and extra documentation; it marks all progress made throughout the year, and is a mapping of process and anaylsis in real-time.

The chosen documentation format for project is markdown, a plain text markup language that can be converted into a multiple of different formats. Github supports markdown and so no conversion is necessary to view documents via a browser. The simplicity of markdown has made it easy to write and commit documents to Github for version control; it also allows for the conversion of documents into another file format using Pandoc[@pandoc]. Written in Haskell, Pandoc is an open-source document converter that is well maintained.

The project was executed on three stages. The first stage being the object detection prototype, the second was the audio retrieval, then the final stage combined the object detection and audio retrieving prototypes. After the prototypes were successfully combined into Flask the final audio triggering was completed. The first stage has been documented [here](https://github.com/DeirdreHegarty/Msc_Project/blob/master/code/app/docs/image_labelling_w1_to_w5.md) and in Appendix A. The remaining stages have been documented [here](https://github.com/DeirdreHegarty/Msc_Project/blob/master/research/Project_Breakdown.md) and in Appendix B.


