# hack-western-9
## Inspiration
1. Affordable pet doors with simple "flap" mechanisms are not secure
2. Potty trained pets requires the door to be manually opened (e.g. ring a bell, scratch the door)

## What it does
The puppy (or cat, we don't discriminate) can exit without approval as soon as the sensor detects an object within the threshold distance. When entering back in, the ultrasonic sensor will trigger a signal that something is at the door and the camera will take a picture and send to the owner's phone through a web app. The owner may approve or deny the request depending on the photo. If the owner approves the request, the door will open automatically.

## How we built it
Ultrasonic sensors relay the distance from the sensor to an object to the Arduino, which sends this signal to Raspberry Pi. The Raspberry Pi program handles the stepper motor movement (rotate ~90 degrees CW and CCW) to open and close the door and relays information to the Flask server to take a picture using the Kinect camera. This photo will display on the web application, where an approval to the request will open the door.

## Challenges we ran into
1. Connecting everything together (Arduino, Raspberry Pi, frontend, backend, Kinect camera) despite each component working well individually
2. Building cardboard prototype with limited resources = lots of tape & poor wire management
3. Using multiple different streams of I/O and interfacing with each concurrently

## Accomplishments that we're proud of
This was super rewarding as it was our first hardware hack! The majority of our challenges lie in the camera component as we're unfamiliar with Kinect but we came up with a hack-y solution and nothing had to be hardcoded.

## What we learned
Hardware projects require a lot of troubleshooting because the sensors will sometimes interfere with eachother or the signals are not processed properly when there is too much noise. Additionally, with multiple different pieces of hardware, we learned how to connect all the subsystems together and interact with the software components.

## What's next for PetAlert
1. Better & more consistent photo quality
2. Improve frontend notification system (consider push notifications)
3. Customize 3D prints to secure components
4. Use thermal instead of ultrasound
5. Add sound detection