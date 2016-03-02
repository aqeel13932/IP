%THIS CODE IS COPIED FROM THIS REPOSITORY 
%https://www.reddit.com/r/matlab/comments/32vfj0/using_interp2_to_resize_an_imageinstead_of/

cd ('/home/aqeel/Study/IP/hw1/')
%M = imread('mupictureorignalgrayscal.png');
M = imread('Obelexorignalgrayscal.png');
t = cputime;
M = double(M);

[Y,X,z] = size(M);
MaxD = max(size(M));
%Scale = 550/MaxD; % create the scale to be applied to both dimensions
Scale = 466/MaxD;
[x,y] = meshgrid(1:X,1:Y); % the grid for the original image

[Xq,Yq] = meshgrid(1:Scale*X,1:Scale*Y); % the grid for the new image

MqR = interp2(x,y,M(:,:,1),Xq,Yq,'spline');
MqG = interp2(x,y,M(:,:,2),Xq,Yq,'spline');
MqB = interp2(x,y,M(:,:,3),Xq,Yq,'spline');

Mq = zeros(floor(Scale*Y),floor(Scale*X),3); % initialize new image matrix

Mq(:,:,1) = MqR;
Mq(:,:,2) = MqG;
Mq(:,:,3) = MqB;

Mq = uint8(Mq);

Xi = linspace(1,X,round(X)*Scale);
Yi = linspace(1,Y,round(Y)*Scale);

[Xq,Yq] = meshgrid(Xi,Yi); % **why do I have to swap the X and Y places in the argument??**

Mq = zeros(floor(Y*Scale),floor(X*Scale),3);

for i = 1:3
    Mq(:,:,i) = interp2(M(:,:,i),Xq,Yq,'spline');
end

Mq = uint8(Mq);
e = cputime-t
imwrite(Mq,'oblexspline.png')
%imwrite(Mq,'mypicturespline.png')