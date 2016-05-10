import cv2
import numpy as np
from math import floor
def showimg(img):
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    img = np.array(img,dtype=float)/float(255)
    cv2.imshow('test',img)
    cv2.resizeWindow('test',600,600)
    cv2.waitKey(0)

def readimg(name):
    return cv2.imread(name)

obe = readimg('Obelix.jpg')

def compressWay1(obe,quality):
    cv2.imwrite('obe_CV2_{}.jpg'.format(quality), obe, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

def compressWay2(obe,quality):
    lvls =floor(quality*255/100)
    step = floor(255/lvls)
    value = floor(step/2)
    print 'levels:{},step:{},value:{},quality:{}'.format(lvls,step,value,quality)
    nm = []
    for i in range(256):
        nm.append(value)
        if i%step==0 and i!=0:
            value+=step
    table = np.array(nm)
    obe = cv2.LUT(obe, table)
    cv2.imwrite('obe_MYWAY_{}.jpg'.format(quality),obe)

compressWay1(obe,10)
compressWay2(obe,10)

