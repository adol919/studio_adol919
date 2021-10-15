"""将图片的人年上的68个标记点显示出来的方法，内在原理似乎是级联分析器"""


import cv2
import dlib


file_path = "image/1.png"
#file_path = "image/family.png"

image = cv2.imread(file_path)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detector = dlib.get_frontal_face_detector()#从dlib中拿到检测人脸的方法
                                        #因为内部原理是使用梯度直方图来检测人脸，所以必须对于灰度图像才有用
#predictor = dlib.shape_predictor("model/shape_predictor_68_face_landmarks.dat")#建立检测轮廓点的方法
predictor = dlib.shape_predictor("model/shape_predictor_5_face_landmarks.dat")

rects = detector(gray,0)#后面一个参数代表放大倍数，放大倍数越大，越能检测到小的人脸

for i,rect in enumerate(rects):
    shape = predictor(gray,rect)

    for index,pt in enumerate(shape.parts()):
        print('Part {}: {}'.format(index, pt))
        pt_pos = (pt.x, pt.y)
        cv2.circle(image, pt_pos, 1, (255, 0, 0), 2)  # 在图片上绘制圆点
        # 利用cv2.putText标注序号

cv2.imshow('face',image)
cv2.waitKey(0)