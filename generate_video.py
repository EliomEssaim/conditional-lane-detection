import cv2
import glob
import os
import argparse

class VideoGenerator():
    def __init__(self) -> None:
        self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description='webcam_sub setting')
        # 自己添加的参数
        parser.add_argument('--path','-p',default='/data/workspace/yelongjie/Project/conditional-lane-detection/',help="determine subscriber topic name")
        parser.add_argument('--node_name','-n',  default="video_sub_py",help="set node_name")
        
        self.args, unknown = parser.parse_known_args()
        

#根据自己的实际情况更改目录。
#要转换的图片的保存地址，按顺序排好，后面会一张一张按顺序读取。

#帧率(fps)，尺寸(size)，此处设置的fps为24，size为图片的大小，本文转换的图片大小为400×1080，
#即宽为400，高为1080，要根据自己的情况修改图片大小。
fps = 24
size = (1640,590)

path='/data/workspace/yelongjie/Project/conditional-lane-detection/'       
selected_dir='show_culane'
video_name = 'driver_100'
path = path + selected_dir
fileList=os.listdir(path)

fileList = [file_name for file_name in fileList if "driver_100_30" in file_name]

fileList.sort()

videopath = '/data/workspace/yelongjie/Project/conditional-lane-detection/' + video_name+ '.avi'

videoWriter = cv2.VideoWriter(videopath,cv2.VideoWriter_fourcc('I','4','2','0'),
                              fps,size)
n = 0
total_number = len(fileList)
for fullname in fileList :
    read_img = cv2.imread(path+'/'+fullname)
    videoWriter.write(read_img)
    print(str(n)+"/"+ str(total_number))
    n=n+1
videoWriter.release()