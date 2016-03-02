__author__ = 'aqeel'
import cv2
import numpy as np
from matplotlib import pyplot as  plt
#img = cv2.imread("Obelix.jpg",cv2.IMREAD_GRAYSCALE)
def LancozOverValues(r,c,window,newimg,oldimg):
    currentrow = floor(r/2+0.5)
    currentcolumn = floor(c/2+0.5)
    xmin= currentrow-window+1
    xmin = (0 if xmin<0 else xmin)
    xmax= currentrow+window
    xmax = (oldimg.shape[0] if xmax>oldimg.shape[0] else xmax)
    ymin= currentcolumn-window+1
    ymin= (0 if ymin<0 else 0)
    ymax= currentcolumn+window+1
    ymax = (oldimg.shape[1] if ymax>oldimg.shape[1] else ymax)

def lanczos2(x):
    #f = (sin(pi*x) .* sin(pi*x/2) + eps) ./ ((pi^2 * x.^2 / 2) + eps);
    #f = f .* (abs(x) < 2);
    result = (np.sin(np.pi*x)*np.sin(np.pi*x/2 +np.spacing(1)))/((np.power(np.pi,2)*np.power(x,2)/2)+np.spacing(1))
    print (np.abs(result)<2)
    result = result*(np.abs(result)<2)
    return result



x = 255
y = np.sinc(x)*np.sinc(x/2)
print y*100
print lanczos2(10)



#Get Doubled image
def GetEmptyDoubleSizeImage(img):
    thenewimg = np.zeros((img.shape[0]*2,img.shape[1]*2),int)
    thenewimg.fill(-1)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            newx = i*2 if i!=0 else i
            newy = j*2 if j!=0 else j
            thenewimg[newx,newy] = img[i,j]
    return thenewimg

def showimg(pimg):
    cv2.imshow('image',pimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def writeimg(filename,pimg):
    cv2.imwrite(filename,pimg)

picture =np.zeros((200,200),dtype=np.uint8)
picture.fill(255)
writeimg('picture.png',picture)
newpicture = GetEmptyDoubleSizeImage(picture)
writeimg('newpicture.png',newpicture)
'''
img = cv2.imread("testimage.jpg",cv2.IMREAD_GRAYSCALE)

resized = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2),interpolation=cv2.INTER_LANCZOS4)
writeimg('resized.png',resized)
writeimg('myresized.png',GetEmptyDoubleSizeImage(img))
print 'newimage:',GetEmptyDoubleSizeImage(img).shape,',original:',img.shape,',autoresize:',resized.shape








print newimage.shape
file = open('newimage.txt','w')
print np.array_str(newimage[0,:])
for i in range (0,newimage.shape[0]):
    file.write(np.array_str(newimage[i,:]))
    file.write('\r\n')

t=''
#print newimage[0,0]

#img = cv2.imread("testimage.jpg",cv2.IMREAD_GRAYSCALE)
# create a mask
#mask = np.zeros(img.shape[:2], np.uint8)
#print 'mask:',mask.shape
#mask[100:600, 100:600] = img[100:600,100:600]
#masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
#hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
#hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
#print hist_mask.shape
#plt.subplot(221), plt.imshow(img, 'gray')
#plt.subplot(222), plt.imshow(mask,'gray')
#plt.subplot(223), plt.imshow(masked_img, 'gray')
#plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
#plt.xlim([0,256])

#plt.show()
#plot histograph with matplotlib
def plotwithmatplot():
    plt.hist(img.ravel(),256,[0,256])
    plt.show()

def ViewImageinWindow():
    cv2.namedWindow('test img',cv2.WINDOW_NORMAL)
    cv2.imshow('test img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#ViewImageinWindow()
'''