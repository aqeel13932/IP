import cv2
import numpy as np
from math import pow


def showimg(img):
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    img = np.array(img,dtype=float)/float(255)
    cv2.imshow('test',img)
    cv2.resizeWindow('test',600,600)
    cv2.waitKey(0)

def readimg(name):
    return cv2.imread(name,0)
#Read The image
mypic = readimg('mypicture.jpg')
resized = cv2.resize(mypic,(512,512),interpolation=cv2.INTER_LANCZOS4)
cv2.imwrite('mypicture_resized.jpg',resized )
for i in range(4,10):
    limit =  int(pow(2,i))
    imagetoresize = np.copy(resized)
    imagetoresize[0:limit,0:limit] = cv2.GaussianBlur(resized[0:limit,0:limit],(5,5),30)
    cv2.imwrite('blurred_piece_by_piece'+str(limit)+'.jpg',imagetoresize)
    #print limit