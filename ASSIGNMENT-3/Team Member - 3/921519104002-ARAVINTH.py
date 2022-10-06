from machine import Pin
from utime import sleep

print("Hello, Pi Pico!")

red = Pin(1, Pin.OUT)
yellow = Pin(5, Pin.OUT)
green = Pin(9, Pin.OUT)
while True:
  red.toggle()
  sleep(1)
  yellow.toggle()
  sleep(1.5)
  green.toggle()
  sleep(2)
