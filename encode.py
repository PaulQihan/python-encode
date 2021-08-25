import subprocess as sp
import cv2 as cv

class Encoder:
    def __init__(self, height, width, fps, url):
        # 推流地址
        self.url = url
        self.height = height
        self.width = width
        self.fps = fps
        self.command = ['ffmpeg',
            '-y',
            '-f', 'rawvideo',
            '-vcodec','rawvideo',
            '-pix_fmt', 'bgr24', # 输入的格式
            '-s', "{}x{}".format(self.width, self.height), # 宽高
            '-r', str(self.fps), # 输入视频的帧率
            '-i', '-',
            '-b:v', '1000k', # 输出视频的码率
            '-f', 'flv', 
            self.url]
        self.pipe = sp.Popen(self.command, stdin=sp.PIPE)
        self.frame_count = 0

    def encode(self, frame):
       self.pipe.stdin.write(frame.tostring())
       self.frame_count += 1
       return self.frame_count