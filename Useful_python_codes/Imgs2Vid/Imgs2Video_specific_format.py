import cv2, glob, datetime,os, re

img_size = (256, 256)

# 조사할 확장자
extensions = ['*.png', '*.jpg']
basepath = os.getcwd()
query_filenames = ['frame']

files_grabbed_by_format = []
files_grabbed = []
epoch_list = []

# 특정 포맷을 기준으로 filename 리스트 생성
[files_grabbed_by_format.extend(glob.glob(f'{basepath}/**/{extension}', recursive=True)) for extension in extensions]
print(len(files_grabbed_by_format))

for (path, dir, files) in os.walk(basepath):
    for filename in files:
        for i in query_filenames:
            if i in filename:
                files_grabbed.append(os.path.join(path, filename))


for f_name in files_grabbed:
    print('%s' % f_name)
print('\n')

# 최신순으로 리스트 재정렬
for i in range(0, len(files_grabbed)):
    for j in range(0, len(files_grabbed)):
        if datetime.datetime.fromtimestamp(os.path.getmtime(files_grabbed[j])) > datetime.datetime.fromtimestamp(os.path.getmtime(files_grabbed[i])):
            (files_grabbed[i], files_grabbed[j]) = (files_grabbed[j], files_grabbed[i])


# 이미지들을 비디오로 컨버트
savedir = os.getcwd()
image_folder = 'images'
video_name = 'fake1.avi'

frame = cv2.imread(os.path.join(image_folder, files_grabbed[0]))
frame = cv2.resize(frame, img_size)
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(video_name, fourcc, fps=15, frameSize=(width, height))

i=0
for image in files_grabbed:
    imageframe = cv2.imread(os.path.join(image_folder, image))
    imageframe = cv2.resize(imageframe, img_size)
    video.write(imageframe)
    i+=1

cv2.destroyAllWindows()
video.release()
