# GRIP : THE SPARKS FOUNDATION
# Parth Jayant More
# TASK_1 : Color identification in images
# Problem Statement : To implement a color detector which identifies all the colors in an image or video.

# ---------------------------------------------------------------------------------------------------------------------------------

# Importing Libraries

import numpy as np
import pandas as pd
import imutils
import cv2

# Defining and resizing the test image using cv2 and imutils .

img = cv2.imread("img.jpg")
img = imutils.resize(img, width = 1000)

# Using csv file (color_names.csv) in our code.

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('color_names.csv', names=index, header=None)
clicked = False
r = g = b = xpos = ypos = 0

# Identifying Color from image

def identify_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

# Defining function for mouse click

def click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# Showing output to user

cv2.namedWindow('Color Identification')
cv2.setMouseCallback('Color Identification', click)
while(1):
    cv2.imshow("Color Identification",img)
    if (clicked):
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        text = identify_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
       
# Clearing all output windows if user enters "esc" key          
   
    if cv2.waitKey(20) & 0xFF ==27:
        break      
cv2.destroyAllWindows()
