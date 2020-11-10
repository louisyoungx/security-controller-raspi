import RPi.GPIO as GPIO
import time

class Gate_control(object):
    
    def __init__(self, channel=None, times=None):
        if channel == None:
            self.channel = 4
        else:
            self.channel = channel			#引脚号16
        if times == None:
            self.times = 0.5
        else:
            self.times = times
        GPIO.setmode(GPIO.BCM)		#以BCM编码格式
        GPIO.setup(self.channel, GPIO.OUT)      #设置GPIO输出

    def open(self):
        self.run()
        time.sleep(self.times)
        self.close()

    def run(self):
        GPIO.output(self.channel, GPIO.LOW)

    def close(self):
        GPIO.output(self.channel, GPIO.HIGH)

         

        
