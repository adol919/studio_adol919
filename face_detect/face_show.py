"""使用dlib从一个图片中捕捉到人脸区域然后显示出来"""

import cv2
import dlib


#file_path = "image/1.png"
file_path = "image/family.png"

image = cv2.imread(file_path)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detector = dlib.get_frontal_face_detector()#从dlib中拿到检测人脸的方法
                                        #因为内部原理是使用梯度直方图来检测人脸，所以必须对于灰度图像才有用

rects = detector(gray,2)#后面一个参数代表放大倍数，放大倍数越大，越能检测到小的人脸

for i,rect in enumerate(rects):
    x1,x2,x3,x4 = rect.left(),rect.right(),rect.top(),rect.bottom()
    print(x1,x2,x3,x4)
    cv2.rectangle(image,(x1,x3),(x2,x4),(0,255,0),2)#在图像上绘制矩形

cv2.imshow('face',image)
cv2.waitKey(0)