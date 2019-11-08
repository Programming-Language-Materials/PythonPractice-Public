# 디렉토리에서 두 장의 이미지를 받아와 한 장으로 합치는 코드

import cv2
import numpy
import shutil as sh
import os as os

imgAList = os.listdir("D:\dictoryParser\DataSets/1024Testset\TrainA(blur)")
imgBList = os.listdir("D:\dictoryParser\DataSets/1024Testset\TrainB(origin)")

baseNameA = "D:\dictoryParser\DataSets/1024Testset\TrainA(blur)/"
baseNameB = "D:\dictoryParser\DataSets/1024Testset\TrainB(origin)/"

for img_no in range(0,len(imgAList)):
    imA = cv2.imread(baseNameA+imgAList[img_no])
    hA,wA,_ = imA.shape

    imB = cv2.imread(baseNameB+imgBList[img_no])
    hB,wB,_ = imB.shape

    templist = [[[0 for col in range(3)] for row in range(512)]for rgb in range(256)]

    newImage = numpy.array(templist)
    h,w,_ = newImage.shape

    for height in range(0,h):
        for width in range(0,w):
            if(width<256):
                newImage[height][width] = imA[height][width]
            else:
                newImage[height][width] = imB[height][width-256]

    cv2.imwrite("D:\dictoryParser/tween/"+str(img_no)+".jpg",newImage)
    # sh.move(dirList[1]+imgAList[img_no],"./tween")
    print("file created file name:   ",imgAList[img_no])