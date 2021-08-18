import cv2
import pyautogui as pg
import time
import numpy as np

def getFish(x,y,size,threshold):
    pg.screenshot('img.png',region=(x,y,size,size))
    img=cv2.imread('img.png')
    cv2.imshow('anh',img)
    cv2.waitKey(1)
    t=0
    for x in range(0,size,1):
        for y in range(0,size,1):
            b,g,r=(img[y,x])
            if b==255 and g==255 and r==255:
                t+=1
    if t>threshold:
        return 1
    else:
        return 0

time.sleep(3)
while True:
    time.sleep(0.5) #this is use for avoid lagging
    pg.press('4') #this is for ending the action
    time.sleep(0.2)   #this is to avoid lagging too
    while getFish(870,396,10,10)==0:

        pass
    pg.press('6') #get fish
    time.sleep(4)
    pg.press('5')



