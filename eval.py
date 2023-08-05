# -*- coding: utf-8 -*-
import cv2
import os
import time
import numpy as np


pos = 0
minblue, mingreen, minred, maxblue, maxgreen, maxred =0,0,0,0,0,0

change_image = False

dir_images = 'images'

def nothing(x):
    pass


def trackbar(minblue=0, mingreen=0, minred=0, maxblue=0, maxgreen=0, maxred=0):
    """по умолчанию все значения нули, и только когда переключаешься на другое изображение 
    значения сохраняются с прошлого трекбара """

    cv2.namedWindow( "result")

    cv2.createTrackbar('minb', 'result', minblue, 255, nothing)
    cv2.createTrackbar('ming', 'result', mingreen, 255, nothing)
    cv2.createTrackbar('minr', 'result', minred, 255, nothing)
    cv2.createTrackbar('maxb', 'result', maxblue, 255, nothing)
    cv2.createTrackbar('maxg', 'result', maxgreen, 255, nothing)
    cv2.createTrackbar('maxr', 'result', maxred, 255, nothing)

    global change_image
    change_image = True



# for file in os.listdir(dir_images):
    
#     img = f"images/{file}"
#     frame_input = cv2.imread(img)


while True:
    
    if change_image == False:
        trackbar(minblue, mingreen, minred, maxblue, maxgreen, maxred) #create trackbars
        

    print(pos)
    img = os.listdir(dir_images)[pos]
    frame_input = f"images/{img}"
    frame_input = cv2.imread(frame_input)
    

    
    hsv = cv2.cvtColor(frame_input, cv2.COLOR_BGR2HSV)

    minb = cv2.getTrackbarPos('minb', 'result')
    ming = cv2.getTrackbarPos('ming', 'result')
    minr = cv2.getTrackbarPos('minr', 'result')
    maxb = cv2.getTrackbarPos('maxb', 'result')
    maxg = cv2.getTrackbarPos('maxg', 'result')
    maxr = cv2.getTrackbarPos('maxr', 'result')


    mask = cv2.inRange(hsv,(minb,ming,minr),(maxb,maxg,maxr))
    cv2.imshow('frame_input', frame_input)

    result=cv2.bitwise_and(frame_input,frame_input,mask=mask)
    cv2.imshow('result1', result)



    if cv2.waitKey(1)==ord("a"):
        pos=pos-1
        print("back")
        minblue, mingreen, minred, maxblue, maxgreen, maxred = minb, ming, minr, maxb, maxg, maxr
        change_image = False
        cv2.destroyAllWindows()
        time.sleep(0.5)
       
       
    elif cv2.waitKey(1)==ord("d"):
        pos=pos+1
        print("forward")
        minblue, mingreen, minred, maxblue, maxgreen, maxred = minb, ming, minr, maxb, maxg, maxr
        change_image = False
        cv2.destroyAllWindows()
        time.sleep(0.5)
        
        


        # if cv2.waitKey(1)==ord("q"):
        #     print("exit")
        #     break
        

 
    # spatialRadius = 70
    # colorRadius = 30
    # pyramidLevels = 3
    # imageSegment = cv2.pyrMeanShiftFiltering(frame_input, spatialRadius, colorRadius, pyramidLevels)

    
    #cv2.imshow("MeanShift", imageSegment)
    #cv2.imshow("frame_input", frame_input)
    
    #cv2.waitKey(10000)# /1000 in seconds
    
    # cv2.destroyAllWindows()
    
    





