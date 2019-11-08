import os
import shutil

ParentDir  = os.listdir("./DataSets/")
print(ParentDir)

for number in range(0,len(ParentDir)):
    ImgPath = "./DataSets/"+str(ParentDir[number])+"/240/"+str(ParentDir[number])
    NewFolderPath = "./DataSets/"+str(ParentDir[number])+"/240_30/"
    print("240fps 이미지 경로 : ",ImgPath)
    ImgList = os.listdir(ImgPath)
    print("240fps 이미지 장수 : ",len(os.listdir(ImgPath)))
    print("new Folder path",NewFolderPath)

    forder = os.path.exists(NewFolderPath)
    if not forder:
        os.mkdir(NewFolderPath,0o700)
        print(NewFolderPath, "생성됨")
    else:
        # 이미 폴더가 존재할 경우 해당 폴더를 지우고 다시 생성. 기존 폴더에 존재하는 모든 파일을 지운 후 빈 폴더 생성
        shutil.rmtree(NewFolderPath)
        os.mkdir(NewFolderPath,0o700)
        print(NewFolderPath)
    ImgList = os.listdir(ImgPath)
    for ImgNo in range(0,len(ImgList)):
        count =0
        if((ImgNo+1)%8==0 or ImgNo==0):
            shutil.copy(ImgPath+"/"+ImgList[ImgNo],NewFolderPath)
            # os.rename(ImgPath+"/"+ImgList[ImgNo],ImgPath+ImgList[ImgNo])
