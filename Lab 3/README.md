# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

**Problem:** Baking bread in the oven usually takes several hours and includes multiple rises at different lengths of time and different temperatures. Not only can it be difficult to keep track of the rises and temperatures, ovens that beep both to indicate time and tempuratue changes can be confusing. The smart oven device sketched below would allow the user to enter in the oven related steps and the smart oven would then speak out the steps at each point rather than simply beeping to notify the user without any indication of what the beeping signifies. Each step would begin when the user put the bowl/loaf in the oven (door sensor) and end when the timer for that step goes off (fail safe so nothing burns if the user does not take the loaf out in time). The issue of not understanding the meaning of the beeps is even more pronounced in settings where there are two ovens (e.g. roasting a chicken in the top oven and making bread in the bottom oven).

![Lab3_pt1_storyboard](https://user-images.githubusercontent.com/45234433/136108662-15edaba5-1459-49d5-98a3-ec02c81f9ccc.jpg)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

**Dialogue:**

User: [looks at recipie] Today I am going to bake a loaf of bread. This requires 4 steps in the oven. 
Let me start by entering these steps into the over interface [types in steps]. 
- Step 1: Proof yeast. Set oven to proofing and proof for 5 - 10 minutes
- Stpe 2: First rise. Set oven to proofing and let rise for 1.5 hours
- Step 3: Second rise. Set oven to proofing and let rise for 45 minutes - 1 hour
- Step 4: Bake. Set oven to 350 and bake for 30 - 35 minutes.
- Take bread out of oven to cool.

Device: Ok. Today we are going to make bread in the top oven. First we will proof the yeast, then do the first rise, then the second rise and lastly bake the loaf. The oven will be ready for proofing in 1 minute.

Device: The oven is ready for proofing the yeast, and timer is set for 5 minutes. Place the yeast in the oven and close the oven door to start the timer. 

User: [places loaf in the oven and closes the door]

Device: Step one proofing yeast for 5 minutes is complete. Press yes to add 5 more minutes, or no to finish this step and move on to the next step. 

User: [presses no]

   Alternative | User: [presses yes]
                 Device: 5 more minutes have been added to the timer. [after 5 minutes] Step one proofing yeast for 10 minutes is complete.

Device: The oven is ready for the first rise and the timer is set for one hour and thirty minutes hours. Place the bread in the oven and close the oven door to start the timer. 

User: [places loaf in the oven and closes the door]

Device: Step two letting the bread rise for one hour and thirty minutes is complete. Press yes to add 5 more minutes, or no to finish this step and move on to the next step.

User: [presses no]

   Alternative | User: [presses yes]
                 Device: 5 more minutes have been added to the timer. [after 5 minutes]. Step two letting the bread rise for one hour and thirty-five minutes is complete.


Device: The oven is ready for the second rise and the timer is set for 45 minutes. Place the bread in the oven and close the oven door to start the timer. 

User: [places loaf in the oven and closes the door]

Device: Step three letting the bread rise for a second time for  45 minutes is complete. Press yes to add 15 more minutes, or no to finish this step and move on to the next step.

User: [presses no]
   
   Alternative | User: [presses yes]
                 Device: 15 more minutes have been added to the timer. [after 15 minutes]. Step three letting the bread rise for a second time for one hour is complete.

Device: The oven is ready to begin baking the bread. The temperature has reached 375 farenheight and the timer is set for 30 minutes. Place the bread in the oven and close the oven door to start the timer. 

User: [places loaf in the oven and closes the door]

Device: Step four baking the bread for 30 minutes is complete. Press yes to add 5 more minutes, or no to finish this step take the bread out of the over to cool.

User: [presses no and takes loaf out to cool]
   
   Alternative | User: [presses yes]
                 Device: 5 more minutes have been added to the timer. [after 15 minutes]. Step four baking the bread for 35 minutes is complete.

\*\***Please describe and document your process.**\*\*

### Acting out the dialogue

A recoding of the video can be viewed on youtube with this link: https://youtu.be/IfNCKVnO2AE

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

It was hard to act out the interaction. It was also hard to start the interaction becasue it needs to be initiated by the user and my partner was not sure how to start nor was I. Once we got started it got easier. The dialogue was similar to what I pictured, the biggest difference being that when acting, everything moved much faster and descisions were made more quickly with less time to consider the options. For example I (as the device) was too slow to offer the option to extend the time, my partner had already moved on to the next step.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

The following updates are based on feedback from partners and class peer reviewers:

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
- In part one of the lab I focused on design. My focus for part two is prototyping with the pi, sensors, and oven to make it feel more realistic. 
- Speech should be more fluid and a little bit faster
- Should be an option to overide/stop the system if the user makes a mistake in the process or wants to change the process they set out.
- Device should promt user for recipie to begin interaction.

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
- Add in another interaction that alerts the user that they are almost ready to move on to the next step. In reality people do not usually wait in the kitchen for entire 2+ hour process, so a 'heads up' notification could help.

3. Make a new storyboard, diagram and/or script based on these reflections.

<img width="869" alt="Lab3_storyboard2" src="https://user-images.githubusercontent.com/45234433/137247272-5d5cb957-e38b-487c-a7e0-ee918a568863.png">

<img width="522" alt="Lab3_sketch" src="https://user-images.githubusercontent.com/45234433/137247287-169aa69f-7576-4f31-bfcf-17195b06c105.png">



## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*: The pi and microphone/speaker were sitting in a metal pot ontop of the oven. They were being controlled by a laptop on the other side of the room. While I was not able to incorporate them, I think this system could also incorporate the green and red buttons as shown in the sketch to allow the user to start and pause/stop the process. 

*Include videos or screencaptures of both the system and the controller.*

See video of the interaction here: https://youtu.be/IRbRT5uGjVg

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*
hard to really get the 

Worked well: 1) the text to speech and speech to text, including how the device was situated, made the device clear and easy to understand. 2) the modularity of the files was also helpful. This allowed for the person controlling the device to easily repeat certain portions when the user wanted to hear those steps again.

What didnt work well: In reality the process being simulated takes several hours and has several steps. It was hard to truly replicate that same environment in a short amount of time.

### What worked well about the controller and what didn't?

It was great to be able to control the device out of sight. It was less confusing for people interacting with the device becasue their attention was not directed at the computer/pi. 

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

Timing is extremley important. With the WoZ the interaction felt choppy and less natural, so any ability to make the interactions flow more smoothly would be helpful. Building in more flexability to let users ask off script questions (which in this version were directed to the person controlling the device) would be helpful in a more autonomous system. 


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

Movement might be interesting to capture. For instance to see how many times the user goes near the oven (for instance to look at the bread while it is rizing) in the middle of a step. It would also be interesting to see if the user came down right at the two minute warning or if they wait until the final anouncement at the end of the step (or later!). Finally, it would be interesting to track common recipies and common adjustments to them, and then save those adjustments for the next time that recipie is used by the user, or recommend those changes to other users of that recipie (e.g. if it really need to bake for 35 minutes at 375 rather than 30).

