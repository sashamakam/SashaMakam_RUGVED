import cv2 as cv
import numpy as np
from collections import deque

video = cv.VideoCapture('Ball_Tracking.mp4')
pts = deque(maxlen=27)


while True:
    isTrue, frame = video.read() 

    cv.imshow('ballvid',frame)

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_green = np.array([35,60,60])
    upper_green = np.array([85,255,255])
    mask = cv.inRange(hsv, lower_green,upper_green )


    ball = cv.bitwise_and(frame,frame,mask=mask)

    contours, hierarchies = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


    cv.imshow('ballmoving',ball)


    if len(contours)>0:
        c = max(contours, key=cv.contourArea)

        ((x,y), radius) = cv.minEnclosingCircle(c)
        center = (int(x),int(y))

        if radius>10:
            cv.circle(ball, (int (x),int(y)), int (radius),(0,255,255),2)
            cv.circle(ball, center,5,(0,0,255),-1 )



    pts.appendleft(center)

    for i in range (1,len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue

        cv.line(ball, pts[i-1],pts[i],(0,0,255),1)
    
    cv.imshow('ball lines',ball)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break






