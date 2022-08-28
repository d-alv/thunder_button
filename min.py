# this will be the main program.
from gpiozero import Button
from gpiozero import Buzzer
import time
from datetime import datetime
import os 
import random
import RPi.GPIO as GPIO

bz = Buzzer(4)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class MainClass:
    """the main class to run the programs"""
    def __init__(self):
        #idk put some stuff in here later
        self.bz = bz
        self.random = random
        self.GPIO = GPIO
        self.datetime = datetime
        self.time = time
        self.elapsed_time = 0
        self.start_time = 0
        self.end_time = 0
        self.need_time = 10
        
        
    def run_program(self):
        """function to keep program in loop"""
        while True:
            self.input_state = self.GPIO.input(18)
            self.check_but()
            self.check_time()
            
    def check_but(self):
        self.end_time = self.time.time()
        if self.input_state==False:
            
            print("button pressed!")
            time.sleep(.2)
            if self.elapsed_time >= self.need_time:  # if it's true, current time = beginning time
                self.start_time = time.time()
                #if self.run_timer() == True:
                self.buzz()
                self.play_sound()
                    # now initiate the other things
            
            if self.elapsed_time < self.need_time:
                self.buzz_b()
                
            if self.run_timer() == False:
                self.buzz_b()
        if self.input_state==True:
         #   self.check_time()
         pass
        
    def check_time(self):
        self.end_time = self.time.time()
        self.elapsed_time = self.end_time - self.start_time
        if self.bz.is_active:
            if self.elapsed_time > 4:
                self.bz.off()
        
            
    def buzz(self):
        self.bz.on()
        self.time.sleep(.5)
        self.bz.off()
        self.time.sleep(.5)
        self.bz.on()
        self.time.sleep(.5)
        self.bz.off()
        
        
        
    def buzz_b(self):
        self.bz.on()
        
    
    
    def run_timer(self):
        now = self.datetime.now()
        current_time=now.strftime("%H:%M")
        accepted_times = ["7:40", "7:41", "7:42", "7:43", "7:44", "9:20",
                          "9:21", "9:22", "9:23", "9:24", "11:00","11:01",
                          "11:02", "11:03", "11:04", "13:00","13:01","13:02",
                          "13:03","13:04", "14:35","14:36","14:37","14:38","14:39", "14:49", "14:50", "14:51", "14:52", "14:53"]
        
        if current_time in accepted_times:
            return True
    
    def play_sound(self):
        song_list = ['aplay /home/pi/Desktop/doorbell/light_strike1.wav',
                     'aplay /home/pi/Desktop/doorbell/light3.wav',
                     'aplay /home/pi/Desktop/doorbell/bolt2.wav',
                     'aplay /home/pi/Desktop/doorbell/zap1.wav',
                     'aplay /home/pi/Desktop/doorbell/thunder1.wav']
        song = self.random.choice(song_list)
        os.system(song)
        
        
        
        
    
if __name__ == "__main__":
    mc = MainClass()
    mc.run_program()
            
        