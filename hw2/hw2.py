import cv2
import numpy as np
from math import log,e,exp
def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i/255.0 ) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def log_tranformation(image):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values

    table = np.array([(log((i+1) / 255.0)) * 255
		for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def exp_tranformation(image):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values

    table = np.array([(exp((i+1) / 255.0)) * 255
		for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def showimg(img):
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    cv2.imshow('test',img)
    cv2.resizeWindow('test',600,600)
    cv2.waitKey(0)

def readimg(name):
    return cv2.imread(name,0)

def sve_equalization(img):
    u,s,v =np.linalg.svd(img,0,1)
    ug,sg,vg = np.linalg.svd(np.reshape(np.random.normal(loc=0.5,scale=1,size=img.shape[0]*img.shape[1]),img.shape),0,1)
    epsilon = np.max(sg)/np.max(s)
    epsilon = max(sg)/max(s)
    return np.floor(epsilon*img*255)
    #print epsilon
    #img = img*epsilon


def stretchilumination(img):
    return img*1.5 +5
obelix =readimg('Obelix.jpg')
mypic = readimg('mypicture.jpg')
#showimg(mypic)
print obelix.shape
print mypic.shape
#Gamma 0.5
#cv2.imwrite('mypic_root(0.5).jpg',adjust_gamma(mypic,0.5))
#cv2.imwrite('mypic_power(2).jpg',adjust_gamma(mypic,2))
#cv2.imwrite('ob_root(0.5).jpg',adjust_gamma(obelix,0.5))
#cv2.imwrite('ob_power(2).jpg',adjust_gamma(obelix,2))
#cv2.imwrite('mypic_log.jpg',log_tranformation(mypic))
#cv2.imwrite('oblix_log.jpg',log_tranformation(obelix))
#cv2.imwrite('mypic_exp.jpg',exp_tranformation(mypic))
#cv2.imwrite('obelix_exp.jpg',exp_tranformation(obelix))
#cv2.imwrite('obelix_hist.jpg',cv2.equalizeHist(obelix))
#cv2.imwrite('mypic_hist.jpg',cv2.equalizeHist(mypic))
#showimg(sve_equalization(mypic))
#cv2.imwrite('mypic_sve.jpg',sve_equalization(mypic))
#cv2.imwrite('obelex_sve.jpg',sve_equalization(obelix))
#cv2.imwrite('mypic_linear.jpg',stretchilumination(mypic))
#cv2.imwrite('obelix_linear.jpg',stretchilumination(obelix))


