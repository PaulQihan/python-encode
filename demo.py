from encode import *
import os
import time

dir = "./Camera_B1/"
encoder = Encoder(1024, 1024, 20, "rtmp://127.0.0.1/live/test")
path_list=os.listdir(dir)
path_list.sort()
for file in path_list:
    frame = cv.imread(dir+file)
    print(dir+str(file))
    time.sleep(0.05)
    encoder.encode(frame)
