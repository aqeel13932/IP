import cv2
from time import time

def ViewImageinWindow(pimg):
    cv2.namedWindow('test img',cv2.WINDOW_NORMAL)
    cv2.imshow('test img',pimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

obeleximg = cv2.imread("Obelix.jpg")
r = float(200)/float(obeleximg.shape[1])
dim = (200,int(obeleximg.shape[0]*r))
obeleximg = cv2.resize(obeleximg,dim)
cv2.imwrite("Obelexorignalgrayscal.png",obeleximg)

mypicture = cv2.imread("mypicture.JPG")
r = float(200)/float(mypicture.shape[1])
dim = (200,int(mypicture.shape[0]*r))
print dim
mypicture = cv2.resize(mypicture,dim)
cv2.imwrite("mupictureorignalgrayscal.png",mypicture)
def InterpolateImage(img,way,filename):
    start = time()
    resized = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2),interpolation=way)
    print filename+" : ", (time()-start)*1000000
    cv2.imwrite(filename+".png",resized)

InterpolateImage(obeleximg,cv2.INTER_NEAREST,'ObelexNearst')
InterpolateImage(obeleximg,cv2.INTER_LINEAR,'obelexBilinear')
InterpolateImage(obeleximg,cv2.INTER_CUBIC,'ObelexCubic')
InterpolateImage(obeleximg,cv2.INTER_LANCZOS4,'ObelexLanczos')

InterpolateImage(mypicture,cv2.INTER_NEAREST,'mypictureNearst')
InterpolateImage(mypicture,cv2.INTER_LINEAR,'mypictureBilinear')
InterpolateImage(mypicture,cv2.INTER_CUBIC,'mypictureCubic')
InterpolateImage(mypicture,cv2.INTER_LANCZOS4,'mypictureLanczos')