import random
while(True):
 temp=random.randint(10,100)
 humid=random.randint(10,100)

 print("current temperature:",temp)
 print("current humidity:", humid, "%")
 temp_ref=22
 humid_ref=23
 if temp<temp_ref and humid<humid_ref:
  print("Sound Alarm")
 else:
  print ("Sound off")
 break   
 