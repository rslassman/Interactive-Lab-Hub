# Final Project
Team: Rebecca Lassman (rsl252) & Marvin Edmond (xx)

***Bike Signaling Device Description (working device)***
We created a device that mimics common hand signals cyclists use to signal turning. Typically on a bike to signal a turn the cyclist will stick their arm out to the left if turning left or the right if turning right.
However, using your arm to signal can pose a handful of challenges:
1. The cyclist has less control over the bike with only one hand on the handle bars. This means if something happens suddenly they can not quickly grab their breaks or make a fast turn. This is even more problematic for new cyclists who may not yet be able to balance/ride with one hand at all.
2. A car's turn signals light up making them easier to see. It can be hard to notice a cyclist sticking out their arm in broad daylight, and it's even more difficult or maybe impossible to see in rain/fog or at night. 

To solve these problems we developed an automated turn signal for cyclists. The device has two parts. The first is a small box that gets mounted on the bike handlebars and has left and right buttons. The second part is a reflective vest with a turn signal (mock arm and hand wrapped in neon tape) mounted on the back.
When the cyclist presses the left or right button on the box mounted on the handle bars, the turn signal on the back rotates in the specified direction mimicking the action of sticking out your arm. 
But in this case the 'arm' allows the cyclist to keep both hands on the handlebars and the neon coating makes it easier for cars to detect. Once the directional button is pressed, the 'arm' remains pointing in the specified direction for 5 seconds then returns to the middle (or straight) position until the next direction is specified. 


***Brainstorming: How we got here***
Through the course of this project we were interested in exploring/creating devices that could better keep cyclists safe while riding on the street. As cyclists we felt like turning was one of the most dangerous aspects of riding on streets with cars so we wanted to address this problem. 
One idea we came up with was a signaling system that could be remotely controlled from the handle bars and display the signal on the cyclists back. We came up with a few possible versions of both the remote and the back display.  

Potential handlebar remote capabilities
- Only left and right buttons
- Left and right buttons with a GPS navigator screen showing your route
- Left and right buttons with GPS navigator screen showing route and possibility for back signal to sync with GPS to signal automatically based on the cyclists route without the need for the cyclists to press the turn signal buttons

See sketches of the handlebar remote in files.


Potential back display options
- Cardboard cutouts of an arrow mounted on the servo moving left/right
- Cardboard cutouts of arms/hand mounted on the servo moving left/right
- Large flexible lightweight LED screen mounted on vest displaying direction signals (arrows, pointers, fade in/flash the specified turning direction like a car light)
- Large flexible lightweight LED screen mounted on vest displaying direction signals (arrows, pointers, fade in/flash the specified turning direction like a car light) with added capability of displaying any message set by the user (e.g. I love NYC)

See sketches of the back display in files.

In terms of communicating between the two devices, the idea is for the handlebar remote to send messages using MQTT and for the back display to read from MQTT and implement the action.


***Technical Implementation***



***Changes From the First Iteration***
- In the first version we used a fabric vest. For the final we got the actual reflective vest which made the device much more realistic. However, even using the fabric vest made us think about how we would need to attach and hide different pieces of the device on the vest. 
- While we were prototyping we were debating between using red and green buttons as opposed to the touch sensors. We decided to use the touch sensor because 1) it requires a lighter touch which we think is a benefit so the person can keep both hands on the handlebars more easily, 2) we could make the size of the touchpad much larger than the size of the button which for the same reason, ease of use, we thought was important, 3) we did not want to associate red and green with left and right, we thought that would be confusing for the user, and 4) the touch sensor fit better in the box. 
- In the first iteration the remote control box with the buttons and 'gps' mounted on the handlebars was much bigger - too big. In the next version we made the device as small as possible (given all of the sensors and wires and pi hiding inside).


***More User Testing and Feedback***
Over the last two weeks we tested the device with a handful of people. 



***Reflection***
What have you learned or wish you knew at the start of the project?




Reflective vest:


Project plan - November 22

Peer feedback on Project plans: November 24

Functional check-off - November 30 & December 2

Final Project Presentations - December 7

Write-up and documentation due - December 13

## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description
Your project is to design and build an interactive device to suit a specific application of your choosing, and test the interaction with people. 
## Deliverables

1. Project plan: Big idea, timeline, parts needed, fall-back plan.

2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

3. Documentation of design process
4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
5. Video of someone using your project
6. Reflections on process (What have you learned or wish you knew at the start?)

7. Group work distribution questionnaire
