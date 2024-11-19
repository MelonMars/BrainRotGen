# BrainRot Gen
![BrainRot Gen](https://cloud-quhfsqm31-hack-club-bot.vercel.app/0screenshot_2024-11-19_173354.png)
This is a simple BrainRot generator. It currently is designed to make those weird videos. You supply videos to it and text to it and it will generate an output video from it.

You can right click within the canvas to create either text or a video, how ever many you like. You control what the text says, and it will be cropped on the screen to demonstate what it will look like, but the text will be saved. text_per_segment determines how much text is shown at a time, and segment_duration determines for how long. Additionally, you can set the source and size of the videos in the rects. These will all be returned to you from the api.  
## Run for yourself:
Install ImageMagick, and find the path to either `convert` or to `imagemagick.exe`
```bash
python api.py IMAGEMAGICKPATH # Replace IMAGEMAGICKPATH with the path to the ImageMagick executable
```
You can then find a webserver of your liking (I've been using the built in WebStorm webserver) and open the index.html file



##### Currently it does not support the AI features, as I'm having problem with my credits, but it will when I fix those. On my computer the AI works.


I would host it myself, but it costs too much, and all the free stuff don't let me run python w/o a credit card...