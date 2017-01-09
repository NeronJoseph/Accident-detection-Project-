#Import necessary packages
import numpy as np
import cv2
from gsm import phoneSms
import math, operator

#Function to find difference in frames
def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

j=1
#Import video from webcam
cam = cv2.VideoCapture(0)

#Creating window to display 
winName = "Accident Detector"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

#Reading frames at multiple instances from webcam to different variables
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


while True:
  #Display video out through the window we created
  cv2.imshow( winName, diffImg(t_minus, t, t_plus) )
  
  #Calling function diffImg() and assign the return value to 'p'
  p=diffImg(t_minus, t, t_plus)
  
  #Writing 'p' to a directory
  cv2.imwrite("D:\photos\shot.jpg",p)
  
  #From Python Image Library(PIL) import Image class
  from PIL import Image
  
  #Open image from the directories and returns it's histogram's
  h1 = Image.open("D:\motionpic\shot"+str(j)+".jpg").histogram()
  h2 = Image.open("D:\photos\shot.jpg").histogram()
  j=j+1

  #Finding rms value of the two images opened before		
  rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))  
  print int(rms)
  
  #If the RMS value of the images are under our limit 
  if (rms<250):
	#Then there is a similarity between images. i.e., Scene similar to an accident is found
	print "accident\a"
	
	#Calls script to send SMS to the specified number
	phoneSms()

  #Updates the frames
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  
  #Destroys the window after key press
  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break  