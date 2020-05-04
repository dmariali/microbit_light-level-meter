# microbit_light-level-meter
Use a microbit to read in light level to ensure houseplants are getting the necessary amount of light

Connect microbit to its' battery pack and place it in the same location as your houseplant. 

Environment Setup : 
pip install virtualenv
virtualenv venv // create virtual environment
source venv/bin/activate  // activate the virtual environment
pip install requirements.txt // if this fails manually pip install all the required packages from requirements.txt
cd microbit
pip install pyserial
python manage.py runserver

VERSION 1 - read temperature in surroundings on microbit and pass that temperature into python file - needs to be moved into django to connect everything. 

NOTES : 
- Connect microbit to your computer via USB 

- go to makecode.microbit.org and do a forever loop sending a variable of your choice via serial 

- download and send to your microbit, if you want you can do 2, one getting info and sending to the one connected to your computer (via radio) 

- with microbit still connected, go to terminal and do lsusb, look for NXP ARM mbed on the list 

- dmesg | grep tty , to find which port your microbit is plugged in (most likely ttyACM0) 

- sudo screen /dev/ttyACM0 115200 (sudo apt-get install screen if you don't already have screen) 

- you should see the output from your microbit being printed out, press CTRL+A then CTRL +D to exit 

- if you get no permission issue do sudo chmod a+rw /dev/ttyACM0 , this gives you permission to access it 

- sudo usermod -aG dialout <username> , then restart your machine. in terminal type groups and you should see 'dialout' on the list 

- Once all this goes well you should be able to run it and get the output from your microbit 

Notes for setup on Mac

- to make sure the connected microbit is receiving data through the serial port, we first need to determine with port it is on.
This port will be of the form cu.