import cv2
import numpy as np
import os

directory = 'Posters'
img1 = cv2.imread("asd.jpg")


foundFile=""

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        img2=cv2.imread('f')

        diff=cv2.subtract(img1,img2)

        result=not np.any(diff)
        if result is True:
            print ("Image Found!!!")
            foundFile=f
        else:
            cv2.imwrite("result.jpg",diff)
            print("No Image Found")

# img2=cv2.imread('Posters/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg')

# #outputimage
# cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("img2", 600, 600)
# cv2.imshow('img2',img2)
# cv2.waitKey(0)

# #inputImage
# cv2.namedWindow("img1", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("img1", 600, 600)
# cv2.imshow('img1',img1)
# cv2.waitKey(0)