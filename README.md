# video_trimmer
python script that trims a video passed as a command line argument
Usage:
python videoTrimmer.py [video_to_trim] [start_time] [end_time] [video_to_save_to]

[start_time] must be a real number or integer
[end_time] can be a real number, an integer or none
if [end_time] is none the video will be trimmed
from [start_time] to the end
if [video_to_save_to] is not provided the clip will be saved to 
[video_to_trim_trimmmed] in the same directory as [video_to_trim]

Example:
python videoTrimmer.py video.mp4 19 1200 trimmed.mp4
