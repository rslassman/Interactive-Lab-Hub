# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***


Contour detection image:<img width="1435" alt="lab5_contours_img" src="https://user-images.githubusercontent.com/45234433/139720773-50a0d5b6-84dd-483e-bdee-b54b55f0361d.png">

**Contour detection design idea**: create a camera/device than can convert a collection of pictures taken on the camera into a coloring book (i.e. with black outlines and a white background). 
![lab5_contors_design_sketch](https://user-images.githubusercontent.com/45234433/139721382-2d4ea3e2-09ab-4dde-a4a5-9595534f761d.jpg)

Face detection image: <img width="1078" alt="lab5_face_detect_img" src="https://user-images.githubusercontent.com/45234433/139764100-14258fec-0c08-4964-86fd-a924244e0959.png">
**Face detection design idea**: use face detection in large spaces to detect how many people are in the room. For example at a concert or especially at non-ticketed events this can help event planners/building owners understand how many people attended.

Optical flow image: <img width="1401" alt="lab5_optical_flow_img" src="https://user-images.githubusercontent.com/45234433/139720719-86b75c23-fdf0-4ff1-b3d8-3b0cfcb59f01.png">
**Optical flow design idea**: create a device that reminds people to look up. I can picture two scenarios:
1. a person who is walking and texting who forgets to look up and see if they are going to bump into people/cars/polls etc. The device could be installed in the phone camera and if more than a certain amount of time passes without the user looking up (could be calibrated to the environment) then the phone could either send a text message or beep or verbally send a message to the user to look up. 
2. when on a hike or walking a lot of times people are focused on where to put their feet next or going fast and miss the sights. This device, maybe on the persons shoes (?) could track their eye movements and again if after a certain amount of time they havent looked up it can somehow send them a message (shoe vibration, ping, verbal message etc.)

Object detection iamge:<img width="1311" alt="lab5_object_detection_img" src="https://user-images.githubusercontent.com/45234433/139720842-0f419471-a08b-40d3-8918-d094ed6b835c.png">
**Object detection design idea**: use object detection in parking lot and street cameras to can identify whether or not parking spaces are occupied or empty. A camera that looks over an entire parking level or street using object dection would be able to tell us exactly which spaces are occupied and which are free. This could then feed into a 'spot finder' app/user interface to help guide drivers directly to open parking spaces 






#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

Media pipe images:

![lab5_pinch_0](https://user-images.githubusercontent.com/45234433/139721207-421e4aed-fc1b-4114-ad07-43f9f5b7011b.png)

![lab5_pinch_98](https://user-images.githubusercontent.com/45234433/139721222-ed1bc59e-04da-474d-9bd8-ac31d3117b0f.png)

![lab5_quiet_coyote](https://user-images.githubusercontent.com/45234433/139721233-2915a3a5-4902-4c32-b939-168a9a7fa4c8.png)

**Media pipe design ideas:** one way to use the percentage control could be to control opening and closing of windows across the room. For instance the percentage you signal on camera could cause the device to pull the window open by that amount. 


#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

Teachable machines image: ![lab5_teachable_machines_img](https://user-images.githubusercontent.com/45234433/139721679-57dbb6ca-8bd1-44b2-86f3-da3f0e24d135.png)

**Teachable machines design idea:** assuming any number of classes can be used, one interesting use case for the teachable machine (in conjunction with hand post tracking) could be creating a written recording of a conversation being held in sign language. Unlike media pipe this would allow the two users having the conversation to be more flexible in the angle and setting. It is more likley that using teachable machine the algorithm could guess the right hand motion whereas using media pipe it would have to be at the exact right angle to be understood which is not realistic in a real world setting. 

I also trained a model to identify whether the object I was holding was a mug or a water bottle. Similar to the predictions are easier to do and provide more flexability inidentifying the objects. Below are images from the model trained on waterbottle vs mug.
![lab5_waterbottle](https://user-images.githubusercontent.com/45234433/139781624-647f06a4-ddfc-456d-814d-ee84b6db0d41.png)

![lab5_mug](https://user-images.githubusercontent.com/45234433/139781640-71655d61-368a-4225-ac6b-ecc62d2dc298.png)


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

The complete idea for this device is to detect if parking spaces are occupied by cars or are empty. Then to send this information to people looking for parking spaces. To do this I started by creating a small parking lot using cardboard and cars using paper. Then I put the lot in the view of the webcam and tested whether it recognized the objects (cars) in the parking spaces. 

![lab5_parkinglot1](https://user-images.githubusercontent.com/45234433/139783870-c3276f5b-ae1a-42c3-922d-9ec9b47ba85b.jpg)

![lab5_parkinglot2](https://user-images.githubusercontent.com/45234433/139783908-7179dec7-fee7-4608-b723-30d8215ead19.jpg)

I realized using the webcam that the object detector kept on picking up the outline of the cardboard parking lot:

![lab5_parking_cardboard](https://user-images.githubusercontent.com/45234433/139784088-52135c1e-10ad-479a-a48d-cd697771942f.jpg)



Next I tried removing the cardboard parking lot and just moving the cars on the solid color desk top. The results of this test can be seen in this video:
https://youtu.be/_bkF_Zxc9bI 




### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
- it worked better when I removed the cardboard. I also noticed that I needed to be fairly close to the objects. It also very rarely detected all three or four cars and once and more often detected one or two. Seemed to work best right at the begining when all cars were just placed.

3. When does it fail?
- fails to detect all cars at once most of the time. Fails if the camera is too far away or at a different angle. 

5. When it fails, why does it fail?
- this may have to do with the fact that the camera was held by hand and not fully stable. Shadows and other lighting uneveness may also have impacted the detection process. 

7. Based on the behavior you have seen, what other scenarios could cause problems?
- I would guess that different weather patterns (rain, snow, bright sunlight) would all have significant impacts on the ability of the device to see the objects. 


**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
- Ideally when presented to the user there could be a likelhood score and/or it could be aggregated to increase certainty. For instance if could say we are 95% sure there is a space at x, or we are 99% sure there is a space in row y. 

3. How bad would they be impacted by a miss classification?
- A misclassification would be frustrating but they could find another space. The realy challegne would be if they lost faith in the model. However that is still only a challenge for the device and nothing disastrous for the user. 
- another risk is that the space is already taken by the time the user gets there. 

5. How could change your interactive system to address this?/ Are there optimizations you can try to do on your sense-making algorithm?
- could include a rate/review of the user's experience to gauge how they are feeling about the model performance. 
- make adjustments fo rcapacity so that only one person is recommended one space. Direct people to rows with more vacancy to increase their chances of finding a space instead of rows with only one space.



### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for? identifying objects
* What is a good environment for X? lots of light, clear color distinctions
* What is a bad environment for X? no light/all the same colors
* When will X break? not able to identify objects
* When it breaks how will X break? make bad recommendations
* What are other properties/behaviors of X? 
* How does X feel? blocky/delayed


**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

video:
https://youtu.be/_bkF_Zxc9bI 

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
The following video shows the prototyped result. The garage is a two space garage. Cars enter from the left and exit from the right. The two spaces are labeled A1 and A2. When a new car is detected in the entryway they get a ping saying "Welcome to the garage!" followed by a ping that tells them where the closest avaiable parking space is. 

![lab5 2_picture1](https://user-images.githubusercontent.com/45234433/141054794-5fbc2001-1320-4e2b-8539-7539fe6f093b.jpg)

![lab5 2_picture2](https://user-images.githubusercontent.com/45234433/141054805-1fe39fa0-7d74-482a-9ca1-b6b47a077277.jpg)

![lab5 2_picture3](https://user-images.githubusercontent.com/45234433/141054822-87d7907a-bf6b-4f56-8398-ba1fb3c52a10.jpg)

![lab5 2_picture4](https://user-images.githubusercontent.com/45234433/141054832-6e96cc22-348d-486c-9a43-a8957f5c9ce0.jpg)

![lab5 2_picture5](https://user-images.githubusercontent.com/45234433/141054841-c1ef9a8d-2bf6-457a-8b40-deeecd40e10f.jpg)


The video first shows the single car being detected in the lot in space A2. Then a new car is detected in the entrance to the garage. Then the user recieves a ping. The user opens the message to get a welcome note and a recommendation for an open parking space. The user then moves into the spot and the camera now detects two cars in the garage. 

Video: https://youtu.be/8Pl2QAPxlvs

