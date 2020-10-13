import sys
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

print('''Usage:
python videoTrimmer.py [video_to_trim] [start_time] [end_time] [video_to_save_to]

if [end_time] is none the video will be trimmed
from start_time to the end
if [video_to_save_to] is not provided the clip will be saved to 
[video_to_trim_trimmmed]

Example:
python videoTrimmer.py video.mp4 19 1200 trimmed.mp4

NB: start_time and end_time are in seconds
'''
)
print('Start time: %s end time: %s' % (sys.argv[2], sys.argv[3]))

clip = VideoFileClip(sys.argv[1])
duration = clip.duration

try:
    start_time = float(sys.argv[2])
    if sys.argv[3] == 'none':
        end_time = duration
    else:
        end_time = sys.argv[3]
except ValueError as error:
    print('Start or end time invalid')

if len(sys.argv) == 4: # no video_to_save_to
    filename = os.path.basename(sys.argv[1])
    filename = filename.split('.')[0] + '_trimmed.mp4'
    ffmpeg_extract_subclip( sys.argv[1], start_time, end_time, targetname=os.path.join(os.path.dirname(sys.argv[1]), filename) )

elif len(sys.argv) == 5:
    ffmpeg_extract_subclip(sys.argv[1], start_time, end_time, targetname=sys.argv[4])