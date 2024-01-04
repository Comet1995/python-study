import os

from pyffmpeg import FFmpeg

f = "D:\下载\小米云盘下载"
fs = os.listdir(f)
for f1 in fs:
    tmp_path = os.path.join(f,f1)
    if not os.path.isdir(tmp_path):
        print(tmp_path)
        ff = FFmpeg('D:\下载\小米云盘下载')
        output_file = ff.convert(inp, out)
        print(output_file)