# date 10th of May, 2021
# onurcan köken
# references:
# https://zulko.github.io/moviepy/_modules/moviepy/Clip.html
# https://www.geeksforgeeks.org/moviepy-setting-end-time-of-the-clip/
# pip install MoviePy

from moviepy.editor import *

path = "video.mp4"
clip = VideoFileClip(path)

# between 5-10 seconds
start_time = 5
end_time = 10
clip = clip.subclip(start_time, end_time)

# resize 75%
clip = clip.resize(0.75)

# specify fps
clip = clip.set_fps(10)

# write as gif format
clip.write_gif("output.gif")