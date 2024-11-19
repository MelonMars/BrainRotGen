# BrainRot Gen

This is a simple BrainRot generator. It currently is designed to make those weird videos. You supply videos to it and text to it and it will generate an output video from it.

Currently it is functioning at: [Firebase](). ***Please*** try to be soft with my server, it's not free for me. And be *very* patient, it takes a while.

If my instance doesn't work for a while, check the console, and if there's an error about the compose, then message me (@Carter Pfaff on Slack) and try running it yourself -- my server is the problem.

## Run for yourself:
The following will work in Linux, and should work pretty similarly in Windows (I am using a VPS so other people can use it):
Requires:
    - Docker
    - Imagemagick

You need to make sure that in api.py, IMAGEMAGICK_BINARY is set to the path of the convert binary. You can find this by running `which convert` in the terminal for Linux, and in windows, just find it yourself (it should be around where it currently is).

Keep in mind the Dockerfile, as written, only works for Linux, you would need to change how the the code installs ImageMagick when using windows. The reason I don't have a Windows version is because if you're on Windows, just run everything locally (just do python3 api.py), and if you want to use a VPS then just use Linux, it's better for VPSes anyway.
```bash
cd Backend
cp /usr/bin/convert ~/my_convert # Replace this with your real imagemagick path
docker build -t brainrotgen .
docker run -d -p 5000:5000 -v ~/my_convert:/usr/bin/convert brainrotgen # -d is optional, it runs everything "detached" so you can close the terminal
```
You can then find a webserver of your liking (I've been using the built in WebStorm webserver) and open the index.html file

To spin down the docker container, if you didn't run with `-d`, then you can just close the terminal. If you did, then you can run `docker ps` to find the container id and then `docker stop <container id>` to stop it.






##### Currently it does not support the AI features, as I'm having problem with my credits, but it will when I fix those. On my computer the AI works.