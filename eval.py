
import cv2
import os
import numpy as np

minblue, mingreen, minred, maxblue, maxgreen, maxred = 151, 255, 0, 255, 255, 255

#minblue, mingreen, minred, maxblue, maxgreen, maxred = 0,0,0,0,0,0

pos = 0 


change_image = False

dir_images = 'images' 

sought = [254,254,254]


def nothing(x):
    ...


def trackbar(minblue=0, mingreen=0, minred=0, maxblue=0, maxgreen=0, maxred=0):

    cv2.namedWindow( "result")
    cv2.createTrackbar('minb', 'result', minblue, 255, nothing)
    cv2.createTrackbar('ming', 'result', mingreen, 255, nothing)
    cv2.createTrackbar('minr', 'result', minred, 255, nothing)
    cv2.createTrackbar('maxb', 'result', maxblue, 255, nothing)
    cv2.createTrackbar('maxg', 'result', maxgreen, 255, nothing)
    cv2.createTrackbar('maxr', 'result', maxred, 255, nothing)

    global change_image
    change_image = True


number_of_files = len(os.listdir(dir_images))
print(f"Всего файлов {number_of_files}")


while True:
    
    if change_image == False:
        trackbar(minblue, mingreen, minred, maxblue, maxgreen, maxred) #create trackbars
    
        
    img = os.listdir(dir_images)[pos]
    frame_input = f"images/{img}"
    frame_input = cv2.imread(frame_input)

    hsv = cv2.cvtColor(frame_input, cv2.COLOR_BGR2HSV)
    color_tone_input = hsv[:,:,0]
    color_tone_input = np.sum(color_tone_input)

    minb = cv2.getTrackbarPos('minb', 'result')
    ming = cv2.getTrackbarPos('ming', 'result')
    minr = cv2.getTrackbarPos('minr', 'result')
    maxb = cv2.getTrackbarPos('maxb', 'result')
    maxg = cv2.getTrackbarPos('maxg', 'result')
    maxr = cv2.getTrackbarPos('maxr', 'result')


    mask = cv2.inRange(hsv,(minb,ming,minr),(maxb,maxg,maxr))
    

    result=cv2.bitwise_and(frame_input,frame_input,mask=mask)

    result = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
    color_tone_result = result[:,:,0]
    color_tone_result = np.sum(color_tone_result)

    proportion = int((color_tone_result / color_tone_input) * 100)
    #print(proportion)

    if proportion in range(5, 200):
        print("stop")
    else:
        print("turn ")

    cv2.imshow('result1', result)
    cv2.imshow('frame_input', frame_input)
    cv2.imshow('mask', mask)
    
    
    
    k = cv2.waitKey(1)

    if k == ord('a'):
        pos=pos-1

        if pos < 0:
            pos = 0
            print("the first file is open")
            
        else:
            minblue, mingreen, minred, maxblue, maxgreen, maxred = minb, ming, minr, maxb, maxg, maxr
            change_image = False
            cv2.destroyAllWindows()
       
       
       
    elif k == ord('d'):

        pos=pos+1

        if pos == number_of_files:
            pos = number_of_files - 1
            print("files are over")

        else:
            minblue, mingreen, minred, maxblue, maxgreen, maxred = minb, ming, minr, maxb, maxg, maxr
            change_image = False
            cv2.destroyAllWindows()
       
    
        

 
 
    
    





