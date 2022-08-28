# thunder_button
Programs for the spirit week button

Concept is simple.

This was created for 2022 Winter olympics hallway decorations

Theme: Greek Gods : Zeus

The user presses the button, this triggers the Active Buzzer to beep twice,
(this was both to notify the user that the button was successfully pressed, 
and also for troubleshooting in case the bluetooth failed, but the program worked), 
then with the onboard RTC module, the raspberry pi kept track of time without wifi.

When the button is pressed, the robot would check the time, so that it would only 
continue if the button was pressed during passing time, so that classes would not 
be disturbed. 

So, when button is pressed, it checks the time to see if it is in the list of 
allowed times, if in list of allowed times, then it beeps twice to let the user
know that it is working, then it randomly picks from a list of thunder audio WAV 
files. This file is then pushed to the bluetooth speaker and a sound sensitive 
device likely paired with a potentiometer makes lights flicker. 
