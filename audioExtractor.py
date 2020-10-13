#! python3
# audioExtractor.py
# extracts audio from video files

import sys
from moviepy.editor import *
import os

print('''Usage:
python audioExtractor.py [videoToExtractFrom] [audioToSaveTo]
if [audioToSaveTo] is omitted, the audio will be saved
in the video's directory with the video's name.
'''
)
try:
    video = VideoFileClip(sys.argv[1])
    audio = video.audio    
except FileNotFoundError or OSError as error :
    print('Error')

if len(sys.argv) == 2:  # no audioToSaveTo
    fileName = os.path.basename(sys.argv[1])
    fileName = fileName.split('.')[0]
    audio.write_audiofile(os.path.join(os.path.dirname(sys.argv[1]), fileName+'.mp3'))

if len(sys.argv) == 3:
    fileName = sys.argv[2]
    audio.write_audiofile(fileName)
