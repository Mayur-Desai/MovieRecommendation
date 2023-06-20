import cv2
import numpy as np
import os
import pandas as pd
# import inp
directory = 'Posters'

dr = ''


def getinput(filen):
    global dr
    dr = 'Posters\\'+f'{filen}'


# D:\error\Posters\l8lq77bNqJY94JCMPI731jwtDsE.jpg
# get_input('8k8RSMkmGR9Lp6FbKtithM3KIQb.jpg')
    # return dr
print(dr)
# Posters\yoGJo1h3Hl2exXPVcG9UXWDENtX.jpg

img1 = cv2.imread(dr)
# # img1 = cv2.imread('Posters\yoGJo1h3Hl2exXPVcG9UXWDENtX.jpg')
# # input poster
# # filename = '1JaMXfXuVfkt3QMATaZE1jblaKk.jpg'

# # foundFile = ""

# # # for filename in os.listdir(directory):
# # f = 'Poster/'+filename
# # # # if os.path.isfile(f):
# # # print(f)

# # img3 = cv2.imread('Poster/'+filename)
# # cv2.namedWindow("img3", cv2.WINDOW_NORMAL)
# # cv2.resizeWindow("img3", 600, 600)
# # cv2.imshow('img3', img3)
# # cv2.waitKey(0)

# #     img2=cv2.imread('f')

# #     diff=cv2.subtract(img1,img2)

# #     result=not np.any(diff)
# #     if result is True:
# #         print ("Image Found!!!")
# #         foundFile=f
# #     else:
# #         cv2.imwrite("result.jpg",diff)
# #         print("No Image Found")
# # break
# # for filename in os.listdir(directory):
# # img2=cv2.imread('Posters/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg')
# # # img2=cv2.imread('asd2.jpg')

# # diff=cv2.subtract(img1,img2)

# # result=not np.any(diff)
# # if result is True:
# #             print ("Image Found!!!")

# # else:
# #             cv2.imwrite("result.jpg",diff)
# #             print("No Image Found")

# # #outputimage
# # cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
# # cv2.resizeWindow("img2", 600, 600)
# # cv2.imshow('img2',img2)
# # cv2.waitKey(0)

# #inputImage
# # cv2.namedWindow("img1", cv2.WINDOW_NORMAL)
# # cv2.resizeWindow("img1", 600, 600)
# # cv2.imshow('img1',img1)
# # cv2.waitKey(0)


def try_very_hard():
    def check(img_p):
        img2 = cv2.imread('Posters/'+img_p)
    # img2=cv2.imread('asd2.jpg')
        try:
            diff = cv2.subtract(img1, img2)

            result = not np.any(diff)
            if result is True:
                # print("Image Found!!!")
                return img_p
        except:
            return

    for file_name in os.listdir(directory):
        st = f'{file_name}'
        t = check(st)
        if type(t) != type(None):
            break
    return t


def get_movie_id():
    md = pd.read_csv('movies_metadata.csv')
    pr = md['poster_path']
    rc = md['original_title']
    c = 0
    poster_id = try_very_hard()
    poster_id1 = '/'+poster_id
    for i in pr:
        st = f'{i}'
        if st == poster_id1:
            break
        c += 1
    return rc[c]


print(get_movie_id())
# # md=pd. read_csv('./movies_metadata.csv')
# # pr=md['poster_path']
# # print(pr)
