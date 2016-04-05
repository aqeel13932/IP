import cv2
import numpy as np
from math import log,e,exp,pow


def showimg(img):
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    img = np.array(img,dtype=float)/float(255)
    cv2.imshow('test',img)
    cv2.resizeWindow('test',600,600)
    cv2.waitKey(0)

def readimg(name):
    return cv2.imread(name,0)
mypic = readimg('mypicture.jpg')

def NoiseImage(img):
    my_nois = np.reshape(np.random.randint(5,20,img.shape[0]*img.shape[1]),(img.shape[0],img.shape[1]))
    return Fiximage(img+my_nois)

def Fiximage (img):
    img[img>255]=255
    img[img<0]=0
    return img


def distance(u,v):
    return np.sqrt(pow(float(u),2)+pow(float(v),2))

def ILPF(img,d0):
    imginFD = np.fft.fft2(img)
    for i in range(imginFD.shape[0]):
        for j in range(imginFD.shape[1]):
            imginFD[i,j]*=distance(i,j)<=d0

    return  np.array(np.fft.ifft2(imginFD),dtype=int)

def IHPF(img,d0):
    imginFD = np.fft.fft2(img)
    for i in range(imginFD.shape[0]):
        for j in range(imginFD.shape[1]):
            imginFD[i,j]*=distance(i,j)>=d0

    return  np.array(np.fft.ifft2(imginFD),dtype=int)

def GHPF(img,d0):
    imginFD = np.fft.fft2(img)
    imginFD= np.array(imginFD,dtype=complex)
    for i in range(imginFD.shape[0]):
        for j in range(imginFD.shape[1]):
            imginFD[i,j]*=1-exp(-pow(distance(i,j),2)/2*d0)

    return  np.array(np.fft.ifft2(imginFD),dtype=int)


noisedimage = NoiseImage(mypic)
cv2.imwrite('mypic_noised.jpg',noisedimage)
noisedimage = readimg('mypic_noised.jpg')
cv2.imwrite('mypic_ILPF.jpg',ILPF(noisedimage,50))
cv2.imwrite('mypic_IHPF.jpg',IHPF(noisedimage,50))
cv2.imwrite('mypic_GHPF.jpg',GHPF(noisedimage,50))
cv2.imwrite('mypic_GLPF.jpg',cv2.GaussianBlur(noisedimage,(5,5),20))


