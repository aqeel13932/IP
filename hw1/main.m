obilixpicture = imread('Obelexorignalgrayscal.png');
mypicture=imread('mupictureorignalgrayscal.png');

obi_large = imresize(obilixpicture,2,{@lanczos4,4});
mypicturelarge=imresize(mypicture,2,{@lanczos4,4});

imwrite(mypicturelarge,'mypictureLanczos')
imwrite(obi_large,'ObelexLanczos')